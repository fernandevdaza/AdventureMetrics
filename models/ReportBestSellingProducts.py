from models.SalesReport import SalesReport
from db.schema import SalesOrderDetail, SalesOrderHeader, Product
from sqlalchemy import func
import pandas as pd

class ReportBestSellingProducts(SalesReport):

    def __init__(self, session):
        super().__init__(session)

    def get_best_selling_products(self, year, limit=None):
        """
        Obtiene los productos más vendidos en un año específico.

        :param year: Año para filtrar las ventas.
        :param limit: Número máximo de filas a retornar.
        :return: DataFrame con los productos más vendidos.
        """

        year_start_date = str(year) + '-01-01 00:00:00'
        year_end_date = str(year) + '-12-31 23:59:59'

        query = self.session.query(
            SalesOrderDetail.productid,
            Product.name,
            func.sum(SalesOrderDetail.orderqty)
        ).join(SalesOrderHeader, SalesOrderDetail.salesorderid == SalesOrderHeader.salesorderid
        ).join(Product, SalesOrderDetail.productid == Product.productid
        ).filter(
            SalesOrderHeader.orderdate.between(year_start_date, year_end_date)
        ).group_by(
            SalesOrderDetail.productid,
            Product.name
        ).order_by(
            func.sum(SalesOrderDetail.orderqty).desc()
        )

        if limit:
            query = query.limit(limit)

        results = query.all()


        df = pd.DataFrame(results, columns=['productid', 'name', 'total'])
        return df
    
    def save_to_excel(self, df, name):
            super().save_to_excel(df, name)
    
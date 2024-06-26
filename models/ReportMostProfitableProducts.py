from models.SalesReport import SalesReport
from db.schema import SalesOrderDetail, SalesOrderHeader, Product
from sqlalchemy import func, case
import pandas as pd

class ReportMostProfitableProducts(SalesReport):
    def __init__(self, session):
        super().__init__(session)
    
    def get_most_profitable_products(self, year, limit=None):
        """
        Obtiene el top de productos más rentables de la base de datos para un año específico.
        :param year: Año a consultar.
        :param limit: Número de productos a mostrar.
        """
        try:
            year_start_date = str(year) + '-01-01 00:00:00'
            year_end_date = str(year) + '-12-31 23:59:59'

            query = self.session.query(
                    Product.name.label('product_name'),
                    func.round(func.sum(SalesOrderDetail.unitprice * SalesOrderDetail.orderqty), 2).label('total_revenue')
            ).join(
                SalesOrderDetail, SalesOrderDetail.productid == Product.productid
            ).join(
                SalesOrderHeader, SalesOrderDetail.salesorderid == SalesOrderHeader.salesorderid
            ).filter(
                SalesOrderHeader.orderdate.between(year_start_date, year_end_date)
            ).group_by(
                Product.name
            ).order_by(
                func.round(func.sum(SalesOrderDetail.unitprice * SalesOrderDetail.orderqty), 2).desc()
            )

            if limit:
                query = query.limit(limit)

            results = query.all()

            df = pd.DataFrame(results, columns=['Producto', 'Total_ganancias'])
            
            
            return df
        except Exception as e:
            raise Exception(f"Error al obtener los productos más rentables: {e}")
        
    def save_to_excel(self, df, name):
            super().save_to_excel(df, name)
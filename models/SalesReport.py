import pandas as pd
from db.connection import SessionLocal
from sqlalchemy import func
from db.schema import SalesOrderDetail, SalesOrderHeader, Product

class SalesReport:

    def __init__(self):
        self.session = SessionLocal()

    def get_date_range(self):
        """
        Obtiene el rango de fechas de las ventas.
        :return: Tupla con la fecha de inicio y fin de las ventas.
        """
        try:
            start_date = self.session.query(func.min(SalesOrderHeader.orderdate)).scalar()
            end_date = self.session.query(func.max(SalesOrderHeader.orderdate)).scalar()
            return start_date, end_date
        except Exception as e:
            raise Exception(f"Error al obtener el rango de fechas: {e}")
    
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


    def close(self):
        self.session.close()
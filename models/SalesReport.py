import pandas as pd
from db.connection import SessionLocal
from sqlalchemy import func, text, case
from db.schema import SalesOrderDetail, SalesOrderHeader, Product

class SalesReport:

    def __init__(self):
        self.session = SessionLocal()
        self.session.execute(text("SET lc_time = 'es_ES.UTF-8'"))

    def get_date_range(self):
        """
        Obtiene el rango de fechas de las ventas en la base de datos.
        :return: Tupla con la fecha de inicio y fin de las ventas.
        """
        try:
            start_date = self.session.query(func.min(SalesOrderHeader.orderdate)).scalar()
            end_date = self.session.query(func.max(SalesOrderHeader.orderdate)).scalar()
            return start_date, end_date
        except Exception as e:
            raise Exception(f"Error al obtener el rango de fechas: {e}")

    def has_data_for_quarter(self, year, quarter):
        """
        Verifica si hay datos para el año y trimestre especificados.
        :param year: Año a verificar.
        :param quarter: Trimestre a verificar.
        """
        try:
            quarter_start_month = (quarter - 1) * 3 + 1
            quarter_end_month = quarter * 3

            start_date = f"{year}-{quarter_start_month:02d}-01"
            if quarter_end_month == 12:
                end_date = f"{year}-12-31"
            else:
                end_date = f"{year}-{quarter_end_month + 1:02d}-01"

            result = self.session.query(SalesOrderHeader).filter(
                SalesOrderHeader.orderdate.between(start_date, end_date)
            ).first()

            return result is not None
        except Exception as e:
            raise Exception(f"Error al verificar datos para el trimestre: {e}")
    
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
    
    def get_seasonal_trends_by_quarter(self, year, quarter=None, limit=None):
        """
        Obtiene el top de productos por trimestre de la base de datos para un año específico.
        :param year: Año a consultar.
        :param quarter: Trimestre a consultar.
        :param limit: Número de productos a mostrar.
        """
        try:
            year_start_date = str(year) + '-01-01 00:00:00'
            year_end_date = str(year) + '-12-31 23:59:59'
            quarter_case = case(
                (func.extract('quarter', SalesOrderHeader.orderdate) == 1, 'Q1'),
                (func.extract('quarter', SalesOrderHeader.orderdate) == 2, 'Q2'),
                (func.extract('quarter', SalesOrderHeader.orderdate) == 3, 'Q3'),
                (func.extract('quarter', SalesOrderHeader.orderdate) == 4, 'Q4'),
            ).label('quarter')

            query = self.session.query(
                quarter_case,
                Product.name.label('product_name'),
                func.sum(SalesOrderDetail.orderqty).label('total_quantity')
            ).join(
                SalesOrderDetail, SalesOrderHeader.salesorderid == SalesOrderDetail.salesorderid
            ).join(
                Product, SalesOrderDetail.productid == Product.productid
            ).filter(
                SalesOrderHeader.orderdate.between(year_start_date, year_end_date)
            )
            
            if quarter:
                query = query.filter(func.extract('quarter', SalesOrderHeader.orderdate) == quarter)
            
            query = query.group_by(
                quarter_case,
                Product.name
            ).order_by(
                quarter_case,
                func.sum(SalesOrderDetail.orderqty).desc()
            )

            results = query.all()

            df = pd.DataFrame(results, columns=['quarter', 'product_name', 'total_quantity'])
            
            if limit:
                df = df.groupby('quarter').head(limit).reset_index(drop=True)
            
            return df
        except Exception as e:
            raise Exception(f"Error al obtener las tendencias trimestrales: {e}")
    
    def close(self):
        self.session.close()
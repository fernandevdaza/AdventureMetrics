import pandas as pd
from sqlalchemy.orm import sessionmaker
from db.connection import get_engine
from sqlalchemy import func, text, case
from db.schema import SalesOrderDetail, SalesOrderHeader, Product

class SalesReport:

    def __init__(self):
        self.engine = get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
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
    
    def close(self):
        self.session.close()
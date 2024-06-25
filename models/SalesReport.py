import pandas as pd
from sqlalchemy import func, text
from db.schema import SalesOrderHeader
import os
class SalesReport:

    def __init__(self, session):
        self.session = session
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
        
    def save_to_excel(self, df, name):
        """
        Guarda el dataframe en un archivo Excel.
        :param df: Dataframe a guardar.
        """
        folder_path = 'reports'
        if not os.path.exists('reports'):
            os.makedirs('reports')

        file_path = os.path.join(folder_path, f"{name}.xlsx")
        try:
            df.to_excel(file_path, index=False)
            print(f"Archivo guardado exitosamente en: {file_path}")
        except Exception as e:
            raise Exception(f"Error al guardar el archivo Excel: {e}")

    
    def close(self):
        self.session.close()
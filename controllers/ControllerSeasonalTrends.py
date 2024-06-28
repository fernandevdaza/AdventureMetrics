from controllers.SalesReportController import SalesReportController
from datetime import datetime
from models.ReportSeasonalTrends import ReportSeasonalTrends

class ControllerSeasonalTrends(SalesReportController):
        def __init__(self, session):
            super().__init__(session, ReportSeasonalTrends)
    
        def get_seasonal_trends_by_quarter(self, year, quarter=None, limit=None):
            """
            Obtiene las tendencias estacionales de los productos vendidos en un año específico.
            
            :param year: Año para filtrar las ventas.
            :param quarter: Trimestre para filtrar las ventas.
            :param limit: Número máximo de filas a retornar.
            :return: DataFrame con las tendencias estacionales.
            """
            if not self._is_valid_date(year):
                raise Exception("El año/trimestre proporcionado no es válido o no se encuentra en la base de datos.")
            
            df = self.report_model.get_seasonal_trends_by_quarter(year, quarter, limit)
            
            if df.empty:
                raise Exception("No se encontraron productos vendidos para el año especificado.")
            
            return df
        
        def save_to_excel(self, df, name):
            """Guarda el reporte en un archivo Excel."""
            self.report_model.save_to_excel(df, name)
    
        def close(self):
            """Método para cerrar la sesión."""
            self.report_model.close()
from models.SalesReport import SalesReport
from datetime import datetime

class SalesReportController:
    
    def __init__(self, session, report_model):
        self.report_model = report_model(session)


    def _is_valid_date(self, year, quarter=None):
        """
        Valida si el año y el trimestre proporcionados son válidos y existen en la base de datos.
        :param year: Año a validar.
        :param quarter: Trimestre a validar.
        :return: True si el año y el trimestre son válidos y existen en la base de datos, False en caso contrario.
        """
        try:
            start_date, end_date = self.report_model.get_date_range()
            current_year = datetime.now().year
            start_year = start_date.year
            end_year = end_date.year
            
            if not (isinstance(year, int) and start_year <= year <= current_year):
                return False
            
            if quarter:
                if not (1 <= quarter <= 4):
                    return False
                has_data = self.report_model.has_data_for_quarter(year, quarter)
                return has_data
            
            return True
        except Exception as e:
            print(f"Error al validar el año y trimestre: {e}")
            return False

    def close(self):
        """Método para cerrar la sesión."""
        self.report_model.close()

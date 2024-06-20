from models.SalesReport import SalesReport
from datetime import datetime

class SalesReportController:
    
    def __init__(self):
        self.report_model = SalesReport()


    def _is_valid_year(self, year):
        """
        Valida si el año proporcionado es válido.
        :param year: Año a validar.
        :return: True si el año es válido, False en caso contrario
        """
        try:
            start_date, end_date = self.report_model.get_date_range()
            current_year = datetime.now().year
            start_year = start_date.year
            end_year = end_date.year
            return isinstance(year, int) and start_year <= year <= current_year
        except Exception as e:
            print(f"Error al validar el año: {e}")
            return False

    def get_best_selling_products(self, year, limit=None):
        """
        Obtiene los productos más vendidos en un año específico.
        
        :param year: Año para filtrar las ventas.
        :param limit: Número máximo de filas a retornar.
        :return: DataFrame con los productos más vendidos.
        """
        if not self._is_valid_year(year):
            raise ValueError("El año proporcionado no es válido o no se encuentra en la base de datos.")

        df = self.report_model.get_best_selling_products(year, limit)
        
        if df.empty:
            raise ValueError("No se encontraron productos vendidos para el año especificado.")
        
        return df

    def close(self):
        """Método para cerrar la sesión."""
        self.report_model.close()

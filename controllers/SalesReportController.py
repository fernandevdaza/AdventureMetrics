from models.SalesReport import SalesReport
from datetime import datetime

class SalesReportController:
    
    def __init__(self):
        self.report_model = SalesReport()


    def _is_valid_date(self, year, quarter=None):
        """
        Valida si el año y el trimestre proporcionados son válidos y existen en la base de datos.
        :param year: Año a validar.
        :param quarter: Trimestre a validar.
        :return: True si el año y el trimestre son válidos y existen en la base de datos, False en caso contrario.
        """
        try:
            # Validar que el año es un entero y está dentro del rango permitido
            start_date, end_date = self.report_model.get_date_range()
            current_year = datetime.now().year
            start_year = start_date.year
            end_year = end_date.year
            
            if not (isinstance(year, int) and start_year <= year <= current_year):
                return False
            
            if quarter:
                if not (1 <= quarter <= 4):
                    return False
                # Verificar si hay datos para el trimestre y año proporcionados
                has_data = self.report_model.has_data_for_quarter(year, quarter)
                return has_data
            
            return True
        except Exception as e:
            print(f"Error al validar el año y trimestre: {e}")
            return False

    def get_best_selling_products(self, year, limit=None):
        """
        Obtiene los productos más vendidos en un año específico.
        
        :param year: Año para filtrar las ventas.
        :param limit: Número máximo de filas a retornar.
        :return: DataFrame con los productos más vendidos.
        """
        if not self._is_valid_date(year):
            raise ValueError("El año/trimestre proporcionado no es válido o no se encuentra en la base de datos.")

        df = self.report_model.get_best_selling_products(year, limit)
        
        if df.empty:
            raise ValueError("No se encontraron productos vendidos para el año especificado.")
        
        return df

    def get_seasonal_trends_by_quarter(self, year, quarter=None, limit=None):
        """
        Obtiene las tendencias estacionales de los productos vendidos en un año específico.
        
        :param year: Año para filtrar las ventas.
        :param quarter: Trimestre para filtrar las ventas.
        :param limit: Número máximo de filas a retornar.
        :return: DataFrame con las tendencias estacionales.
        """
        if not self._is_valid_date(year):
            raise ValueError("El año/trimestre proporcionado no es válido o no se encuentra en la base de datos.")
        
        df = self.report_model.get_seasonal_trends_by_quarter(year, quarter, limit)
        
        if df.empty:
            raise ValueError("No se encontraron productos vendidos para el año especificado.")
        
        return df

    def close(self):
        """Método para cerrar la sesión."""
        self.report_model.close()

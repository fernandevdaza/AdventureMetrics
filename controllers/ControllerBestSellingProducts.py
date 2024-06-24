from controllers.SalesReportController import SalesReportController
from datetime import datetime
from models.ReportBestSellingProducts import ReportBestSellingProducts
 
class ControllerBestSellingProducts(SalesReportController):

    def __init__(self):
        super().__init__()
        self.report_model = ReportBestSellingProducts()

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

    def close(self):
        """Método para cerrar la sesión."""
        self.report_model.close()
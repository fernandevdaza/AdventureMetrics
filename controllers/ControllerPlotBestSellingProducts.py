from controllers.PlotController import PlotController
class ControllerPlotBestSellingProducts(PlotController):
    def __init__(self, plot_model) -> None:
        super().__init__(plot_model)
    
    def _is_valid_limit(self, limit):
        """
        Valida si el límite proporcionado es un número entero válido y menor o igual a 10.
        :param limit: Límite a validar.
        :return: True si el límite es un número entero válido, False en caso contrario.
        """
        return super()._is_valid_limit(limit)
    
    def plot_best_selling_products(self, df, year, limit):
        """
        Genera un gráfico de los productos más vendidos en un año específico.

        :param year: Año para filtrar las ventas.
        :param limit: Número máximo de filas a graficar.
        :return: None
        """
        if not self._is_valid_limit(limit):
            return None
        return self.plot_model.plot_best_selling_products(df, year, limit)
    
    def limit_rows(self, df, limit):
        """
        Limita el número de filas de un dataframe.
        :param df: Dataframe a limitar.
        :param limit: Número máximo de filas.
        :return: Dataframe con el número de filas limitado.
        """
        return self.plot_model.limit_rows(df, limit)    


    def save_plot(self, plot, name):
        """
        Guarda el gráfico en un archivo.
        """
        self.plot_model.save_plot(plot, name)
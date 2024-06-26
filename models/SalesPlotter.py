import os
class SalesPlotter():
    def __init__(self) -> None:
        pass

    def limit_rows(self, df, limit=10, groupby=None):
        """
        Limita el número de filas de un DataFrame agrupando por una columna.
        :param df: DataFrame a limitar.
        :param limit: Número de filas a mostrar.
        :param groupby: Columna por la cual agrupar.
        """
        if groupby:
            return df.groupby(groupby).head(limit).reset_index(drop=True)
        return df.head(limit)
    
    def save_plot(self, fig, name):
        """
        Guarda un gráfico en un archivo.
        :param fig: Gráfico a guardar.
        :param name: Nombre del archivo.
        """
        folder_path = 'plots'
        if not os.path.exists('plots'):
            os.makedirs('plots')

        file_path = os.path.join(folder_path, f"{name}.png")
        try:
            fig.savefig(file_path)
            print(f"Gráfico guardado exitosamente en: {file_path}")
        except Exception as e:
            raise Exception(f"Error al guardar el gráfico: {e}")
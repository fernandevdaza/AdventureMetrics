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
        
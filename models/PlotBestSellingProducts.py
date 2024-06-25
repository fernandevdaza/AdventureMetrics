from matplotlib import pyplot as plt
from models.SalesReport import SalesReport
from db.schema import SalesOrderDetail, SalesOrderHeader, Product
from sqlalchemy import func
import pandas as pd
from models.SalesPlotter import SalesPlotter

class PlotBestSellingProducts(SalesPlotter):

    def __init__(self):
        super().__init__()

    def plot_best_selling_products(self, df, year, limit=None):
        """
        Genera un gráfico de los productos más vendidos en un año específico.

        :param year: Año para filtrar las ventas.
        :param limit: Número máximo de filas a graficar.
        :return: None
        """
        df = self.limit_rows(df, limit)

        plt.figure(figsize=(10, 6))
        plt.bar(df['name'], df['total'], color='skyblue')
        plt.xlabel('Producto')
        plt.ylabel('Cantidad Vendida')
        plt.title(f'Productos más vendidos en {year}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.show()
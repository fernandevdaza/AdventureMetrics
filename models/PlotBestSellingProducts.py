from matplotlib import pyplot as plt
from models.SalesReport import SalesReport
from db.schema import SalesOrderDetail, SalesOrderHeader, Product
from sqlalchemy import func
import pandas as pd
from models.SalesPlotter import SalesPlotter

class PlotBestSellingProducts(SalesPlotter):

    def __init__(self):
        super().__init__()

    def plot_best_selling_products(self, df, year, limit=10):
        """
        Genera un gráfico de los productos más vendidos en un año específico.

        :param df: DataFrame con los datos a graficar.
        :param year: Año para filtrar las ventas.
        :param limit: Número máximo de filas a graficar.
        :return: Figure object
        """
        df = self.limit_rows(df, limit)

        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Create the bar plot
        bars = ax.bar(range(len(df)), df['Total Vendido'], color='skyblue')
        
        # Set the x-axis ticks and labels
        ax.set_xticks(range(len(df)))
        ax.set_xticklabels(df['Nombre'], rotation=45, ha='right')

        # Adjust the subplot to make room for the rotated labels
        plt.subplots_adjust(bottom=0.2)

        # Label the axes and set the title
        ax.set_xlabel('Producto')
        ax.set_ylabel('Cantidad Vendida')
        ax.set_title(f'Productos más vendidos en {year}')

        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:,.0f}',
                    ha='center', va='bottom')

        # Adjust the layout
        fig.tight_layout()   

        return fig
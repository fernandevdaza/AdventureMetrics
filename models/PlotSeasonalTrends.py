from models.SalesPlotter import SalesPlotter
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
class PlotSeasonalTrends(SalesPlotter):

    def __init__(self) -> None:
        super().__init__()

    def plot_all_quarters(self, df, limit=10):
        df = self.limit_rows(df, limit, 'quarter')

        df_pivot = df.pivot(index='quarter', columns='product_name', values='total_quantity')

        total_sales = df_pivot.sum().sort_values(ascending=False)
        df_pivot = df_pivot[total_sales.index]

        fig, ax = plt.subplots(figsize=(14, 8))
        df_pivot.plot(kind='bar', stacked=True, ax=ax)
        
        ax.set_title('Tendencias trimestrales')
        ax.set_xlabel('Trimestre')
        ax.set_ylabel('Cantidad total')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax.grid(axis='y')
        plt.subplots_adjust(right=0.804)
        return fig
        


    def plot_quarter(self, df, quarter, limit=20):
        df = self.limit_rows(df, limit)

        fig, ax = plt.subplots(figsize=(12, 8))

        df.plot(kind='bar', x='product_name', y='total_quantity', ax=ax, legend=False)

        ax.set_title(f'Tendencias trimestrales - {quarter}')
        ax.set_xlabel('Producto')
        ax.set_ylabel('Cantidad total')
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        ax.grid(axis='y')
        plt.subplots_adjust(bottom=0.347)
        return fig
    
    def save_plot(self, fig, name):
        return super().save_plot(fig, name)
from models.SalesPlotter import SalesPlotter
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
class PlotSeasonalTrends(SalesPlotter):

    def __init__(self) -> None:
        super().__init__()

    def plot_all_quarters(self, df, limit=10):
        # Limit rows
        df = self.limit_rows(df, limit, 'quarter')

        # Pivot the dataframe
        df_pivot = df.pivot(index='quarter', columns='product_name', values='total_quantity')

        # Reorder columns by total sales
        total_sales = df_pivot.sum().sort_values(ascending=False)
        df_pivot = df_pivot[total_sales.index]

        # Plot stacked bar chart
        ax = df_pivot.plot(kind='bar', stacked=True, figsize=(12, 8))
        
        plt.title('Tendencias trimestrales')
        plt.xlabel('Trimestre')
        plt.ylabel('Cantidad total')
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.grid(axis='y')
        plt.show()

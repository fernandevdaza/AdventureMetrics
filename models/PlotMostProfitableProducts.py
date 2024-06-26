from models.SalesPlotter import SalesPlotter
from matplotlib import pyplot as plt


class PlotMostProfitableProducts (SalesPlotter):
    def __init__(self) -> None:
        super().__init__()
    
    def plot_most_profitable_products(self, df, year, limit=10):
        try:
            
            df_copy = self.limit_rows(df, limit)
            
            if df_copy.empty:
                print("No hay datos para mostrar.")
                return None
            
            total_revenue_sum = df_copy['total_revenue'].sum()
            df_copy['percentage'] = (df_copy['total_revenue'] / total_revenue_sum) * 100

            fig, ax = plt.subplots(figsize=(12, 8))
            wedges, texts, autotexts = ax.pie(df_copy['percentage'], 
                                              labels=df_copy['product_name'], 
                                              autopct='%1.1f%%', 
                                              startangle=140,
                                              pctdistance=0.85)

            centre_circle = plt.Circle((0,0), 0.70, fc='white')
            fig.gca().add_artist(centre_circle)

            ax.set_title(f'Top {limit} Most Profitable Products in {year}')
            
            plt.setp(autotexts, size=8, weight="bold")
            plt.setp(texts, size=8)

            ax.legend(wedges, df_copy['product_name'],
                      title="Products",
                      loc="center left",
                      bbox_to_anchor=(1, 0, 0.5, 1))

            plt.tight_layout()

            return fig
        except Exception as e:
            raise Exception(f"Error al generar el gráfico de torta: {e}")


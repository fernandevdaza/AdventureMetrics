from models.SalesPlotter import SalesPlotter
from matplotlib import pyplot as plt


class PlotMostProfitableProducts (SalesPlotter):
    def __init__(self) -> None:
        super().__init__()
    
    def plot_pie_chart(self, df, year, limit=20):
        try:
            df = self.limit_rows(df, limit)
            if df.empty:
                print("No hay datos para mostrar.")
                return
            
            total_revenue_sum = df['total_revenue'].sum()
            df.loc[:, 'percentage'] = (df['total_revenue'] / total_revenue_sum) * 100


            plt.figure(figsize=(10, 8))
            plt.pie(df['percentage'], labels=df['product_name'], autopct='%1.1f%%', startangle=140)
            plt.title(f'Top {limit} Most Profitable Products in {year}')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Mostrar el gráfico
            plt.show()
        except Exception as e:
            raise Exception(f"Error al generar el gráfico de torta: {e}")
            


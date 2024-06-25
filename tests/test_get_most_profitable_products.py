import pandas as pd
from controllers.ControllerMostProfitableProducts import ControllerMostProfitableProducts
from models.PlotMostProfitableProducts import PlotMostProfitableProducts

def test_get_most_profitable_products():
    try:
        year = int(input("Ingrese el año a consultar: "))
        is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")
        
        if is_limited.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar: "))
        else:
            limit = None

        controller = ControllerMostProfitableProducts()
        df = controller.get_most_profitable_products(year, limit)
        print(df)
        print("\n")
        show_plot = input("¿Desea mostrar el gráfico de los productos mas rentables? (s/n): ")
        if show_plot.lower() =='s':
            limit = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 20): "))
            plotter = PlotMostProfitableProducts()
            plotter.plot_pie_chart(df, year, limit)
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        controller.close()

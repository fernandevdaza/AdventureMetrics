import pandas as pd
from controllers.ControllerMostProfitableProducts import ControllerMostProfitableProducts
from controllers.ControllerPlotMostProfitableProducts import ControllerPlotMostProfitableProducts
from models.PlotMostProfitableProducts import PlotMostProfitableProducts
def test_get_most_profitable_products(session):
    try:
        controller = ControllerMostProfitableProducts(session)
        year = int(input("Ingrese el año a consultar: "))
        is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")
        
        if is_limited.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar: "))
        else:
            limit = None

        df = controller.get_most_profitable_products(year, limit)

        if (limit == None) or limit > 20:
            print("Se guardará su reporte en un archivo Excel.")
            controller.save_to_excel(df, 'most_profitable_products')
        else:
            print(df)
            print("\n")
            save_to_excel = input("¿Desea guardar el reporte en un archivo Excel? (s/n): ")
            if save_to_excel.lower() == 's':
                controller.save_to_excel(df, 'most_profitable_products')
            else:
                pass


        print("\n")
        show_plot = input("¿Desea mostrar el gráfico de tendencias trimestrales? (s/n): ")
        if show_plot.lower() == 's':
            limited = None
            if limit == None:
                limited = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 10): "))
            plotter = ControllerPlotMostProfitableProducts(PlotMostProfitableProducts)
            plot = plotter.plot_most_profitable_products(df, year, limited)
            plot.show()
            save_plot = input("¿Desea guardar el gráfico en un archivo? (s/n): ")
            if save_plot.lower() == 's' and plot is not None:
                plotter.save_plot(plot, 'most_profitable_products')
            else:
                pass
        else:
            return
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        controller.close()

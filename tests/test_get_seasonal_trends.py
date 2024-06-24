import pandas as pd
from controllers.ControllerSeasonalTrends import ControllerSeasonalTrends
from models.PlotSeasonalTrends import PlotSeasonalTrends
def test_get_seasonal_trends():
    try:
        year = int(input("Ingrese el año a consultar: "))
        filter_by_quarter = input("¿Desea filtrar por trimestre? (s/n): ")

        if filter_by_quarter.lower() == 's':
            quarter = int(input("Ingrese el trimestre a consultar: "))
        else:
            quarter = None
        
        is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")

        if is_limited.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar: "))
        else:
            limit = None
        controller = ControllerSeasonalTrends()
        df = controller.get_seasonal_trends_by_quarter(year, quarter, limit)
        print(df)

        print("\n")
        show_plot = input("¿Desea mostrar el gráfico de tendencias trimestrales? (s/n): ")
        if show_plot.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 20): "))
            plotter = PlotSeasonalTrends()
            plotter.plot_all_quarters(df, limit)
        else:
            return
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        if controller is not None:
            controller.close()
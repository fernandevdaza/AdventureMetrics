import pandas as pd
from controllers.ControllerSeasonalTrends import ControllerSeasonalTrends
from models.PlotSeasonalTrends import PlotSeasonalTrends
from controllers.ControllerPlotSeasonalTrends import ControllerPlotSeasonalTrends
def test_get_seasonal_trends(session):
    try:
        controller = ControllerSeasonalTrends(session)
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
        df = controller.get_seasonal_trends_by_quarter(year, quarter, limit)


        if (limit == None and quarter == None) or (limit != None and quarter == None) or (limit == None and quarter != None) or limit > 20:
            print("Se guardará su reporte en un archivo Excel.")
            controller.save_to_excel(df, 'seasonal_trends')
        else:
            print(df)
            print("\n")
            save_to_excel = input("¿Desea guardar el reporte en un archivo Excel? (s/n): ")
            if save_to_excel.lower() == 's':
                controller.save_to_excel(df, 'seasonal_trends')
            else:
                pass


        print("\n")
        show_plot = input("¿Desea mostrar el gráfico de tendencias trimestrales? (s/n): ")
        if show_plot.lower() == 's':
            limited = None
            if limit == None:
                limited = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 10): "))
            plotter = ControllerPlotSeasonalTrends(PlotSeasonalTrends)
        # Si filtro en quarter, mostrar el metodo singular de grafico
            if quarter == None:
                plot = plotter.plot_all_quarters(df, limited)
                plot.show()
            else:
                plot = plotter.plot_quarter(df, quarter, limited)
                plot.show()
            save_plot = input("¿Desea guardar el gráfico en un archivo? (s/n): ")
            if save_plot.lower() == 's' and plot is not None:
                plotter.save_plot(plot, 'seasonal_trends')
            else:
                pass
        else:
            return

    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        if controller is not None:
            controller.close()
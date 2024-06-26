from controllers.ControllerSeasonalTrends import ControllerSeasonalTrends
from controllers.ControllerPlotSeasonalTrends import ControllerPlotSeasonalTrends
from models.PlotSeasonalTrends import PlotSeasonalTrends
from user_interface.clear_util import clear

def ui_seasonal_trends(session):
    while True:
        try:
            print("Cargando...")
            clear()
            controller = ControllerSeasonalTrends(session)
            print(r"""
  _____              _                 _             _____     _             _                   _           
 |_   _|__ _ __   __| | ___ _ __   ___(_) __ _ ___  | ____|___| |_ __ _  ___(_) ___  _ __   __ _| | ___  ___ 
   | |/ _ \ '_ \ / _` |/ _ \ '_ \ / __| |/ _` / __| |  _| / __| __/ _` |/ __| |/ _ \| '_ \ / _` | |/ _ \/ __|
   | |  __/ | | | (_| |  __/ | | | (__| | (_| \__ \ | |___\__ \ || (_| | (__| | (_) | | | | (_| | |  __/\__ \
   |_|\___|_| |_|\__,_|\___|_| |_|\___|_|\__,_|___/ |_____|___/\__\__,_|\___|_|\___/|_| |_|\__,_|_|\___||___/                                                                                                
""")
            print("\n")
            print("Por favor, escriba 'Q' para regresar al menú principal.")
            year = input("Ingrese el año para la consulta: ")
            if year.lower() == 'q':
                return
            year = int(year)

            filter_by_quarter = input("¿Desea filtrar por trimestre? (s/n): ")
            if filter_by_quarter.lower() == 's':
                quarter = input("Ingrese el trimestre a consultar: ")
                if quarter.lower() == 'q':
                    return
                quarter = int(quarter)
            else:
                quarter = None

            is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")
            if is_limited.lower() == 's':
                limit = input("Ingrese el número de productos a mostrar: ")
                if limit.lower() == 'q':
                    return
                limit = int(limit)
            else:
                limit = None

            print("\n")
            print("Consultando...espere un momento.")
            print("\n")
            df = controller.get_seasonal_trends_by_quarter(year, quarter, limit)

            if (limit == None and quarter == None) or (limit != None and quarter == None) or (limit == None and quarter != None) or limit > 20:
                print("Se guardará su reporte en un archivo Excel.")
                nombre = input("Ingrese el nombre del archivo: ")
                print("Guardando reporte en un archivo Excel. Un momento por favor...")
                controller.save_to_excel(df, nombre)
            else:
                print(df)
                print("\n")
                save_to_excel = input("¿Desea guardar el reporte en un archivo Excel? (s/n): ")
                if save_to_excel.lower() == 's':
                    nombre = input("Ingrese el nombre del archivo: ")
                    print("Guardando reporte en un archivo Excel. Un momento por favor...")
                    controller.save_to_excel(df, nombre)
                elif save_to_excel.lower() == 'n':
                    pass
                else:
                    raise ValueError("Opción no válida.")

            print("\n")
            plot_seasonal_trends(df, year, quarter, limit)
        except ValueError as e:
            clear()
            print(f"Valor inválido, por favor inténtelo de nuevo")
        except Exception as e:
            clear()
            print(f"Se produjo un error")
        finally:
            if controller is not None:
                controller.close()

def plot_seasonal_trends(df, year, quarter, limit):
    while True:
        try:
            show_plot = input("¿Desea ver un gráfico de las tendencias trimestrales? (s/n): ")
            if show_plot.lower() == 's':
                limited = None
                if limit == None or limit > 10:
                    limited = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 10): "))
                    if limited > 10:
                        raise ValueError("El límite no puede ser mayor a 10.")
                else:
                    limited = limit
                print("Generando gráfico de tendencias trimestrales. Un momento por favor...")
                plotter = ControllerPlotSeasonalTrends(PlotSeasonalTrends)
                if quarter == None:
                    plot = plotter.plot_all_quarters(df, limited)
                else:
                    plot = plotter.plot_quarter(df, quarter, limited)
                plot.show()
                save_plot = input("¿Desea guardar el gráfico en un archivo? (s/n): ")
                if save_plot.lower() == 's' and plot is not None:
                    nombre = input("Ingrese el nombre del archivo: ")
                    print("Guardando gráfico en un archivo. Un momento por favor...")
                    plotter.save_plot(plot, nombre)
                else:
                    pass
            elif show_plot.lower() == 'n':
                return
            else:
                raise ValueError("Opción no válida.")
            print("\n")
            return
        except ValueError as e:
            clear()
            print(f"Valor inválido: {e}")
        except Exception as e:
            clear()
            print(f"Se produjo un error: {e}")
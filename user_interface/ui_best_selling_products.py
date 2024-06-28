from controllers.ControllerBestSellingProducts import ControllerBestSellingProducts
from controllers.ControllerPlotBestSellingProducts import ControllerPlotBestSellingProducts
from models.PlotBestSellingProducts import PlotBestSellingProducts
from user_interface.clear_util import clear
def ui_best_selling_products(session):
    while True:
        try:
            controller = ControllerBestSellingProducts(session)
            print(r"""
                             _ _     _          
   _    __   _____ _ __   __| (_) __| | ___  ___ 
 _| |_  \ \ / / _ \ '_ \ / _` | |/ _` |/ _ \/ __|
|_   _|  \ V /  __/ | | | (_| | | (_| | (_) \__ \
  |_|     \_/ \___|_| |_|\__,_|_|\__,_|\___/|___/                                                                             
    """)
            print("\n")
            print("Por favor, escriba 'Q' para regresar al menú principal.")
            year = input("Ingrese el año para la consulta: ")
            if year.lower() == 'q':
                return
            year = int(year)
            
            is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")
            if is_limited.lower() == 's':
                limit = input("Ingrese el número de productos a mostrar: ")
                if limit.lower() == 'q':
                    return
                limit = int(limit)
            elif is_limited.lower() == 'n':
                limit = None
            else:
                raise ValueError("Opción no válida.")
            
            print("\n")
            print("Consultando...espere un momento.")
            print("\n")
            df = controller.get_best_selling_products(year, limit)
            
            if limit == None or limit > 20:
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
            plot_best_selling_products(df, year, limit)
            clear()
        except ValueError as e:
            clear()
            print(f"Valor inválido, por favor inténtelo de nuevo")
        except Exception as e:
            clear()
            print(f"Se produjo un error")
        finally:
            if controller is not None:
                controller.close()

def plot_best_selling_products(df, year, limit):
    while True:
        try:
            show_plot = input("¿Desea ver un gráfico de los productos más vendidos? (s/n): ")
            if show_plot.lower() == 's':
                limited = None
                if limit == None or limit > 10:
                    limited = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 10): "))
                    if limited > 10:
                        raise ValueError("El límite no puede ser mayor a 10.")
                else:
                    limited = limit
                print("Generando gráfico de productos más vendidos. Un momento por favor...")
                plotter = ControllerPlotBestSellingProducts(PlotBestSellingProducts)
                plot = plotter.plot_best_selling_products(df, year, limited)
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
    
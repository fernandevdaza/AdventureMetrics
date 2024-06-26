from controllers.ControllerBestSellingProducts import ControllerBestSellingProducts
from controllers.ControllerPlotBestSellingProducts import ControllerPlotBestSellingProducts
from models.PlotBestSellingProducts import PlotBestSellingProducts

def ui_best_selling_products(session):
    try:
        controller = ControllerBestSellingProducts(session)
        print(r"""
.___  ___.      ___           _______.   ____    ____  _______ .__   __.  _______   __   _______   ______        _______.
|   \/   |     /   \         /       |   \   \  /   / |   ____||  \ |  | |       \ |  | |       \ /  __  \      /       |
|  \  /  |    /  ^  \       |   (----`    \   \/   /  |  |__   |   \|  | |  .--.  ||  | |  .--.  |  |  |  |    |   (----`
|  |\/|  |   /  /_\  \       \   \         \      /   |   __|  |  . `  | |  |  |  ||  | |  |  |  |  |  |  |     \   \    
|  |  |  |  /  _____  \  .----)   |         \    /    |  |____ |  |\   | |  '--'  ||  | |  '--'  |  `--'  | .----)   |   
|__|  |__| /__/     \__\ |_______/           \__/     |_______||__| \__| |_______/ |__| |_______/ \______/  |_______/                                                                                                                        
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
        else:
            limit = None
        
        print("\n")
        print("Consultando...espere un momento.")
        print("\n")
        df = controller.get_best_selling_products(year, limit)
        
        if limit == None or limit > 20:
            print("Se guardará su reporte en un archivo Excel.")
            controller.save_to_excel(df, 'best_selling_products')
        else:
            print(df)
            print("\n")
            save_to_excel = input("¿Desea guardar el reporte en un archivo Excel? (s/n): ")
            if save_to_excel.lower() == 's':
                print("Guardando reporte en un archivo Excel. Un momento por favor...")
                controller.save_to_excel(df, 'best_selling_products')
            else:
                pass
        
        print("\n")
        show_plot = input("¿Desea ver un gráfico de los productos más vendidos? (s/n): ")
        if show_plot.lower() == 's':
            limited = None
            if limit == None or limit > 10:
                limited = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 10): "))
            else:
                limited = limit
            print("Generando gráfico de productos más vendidos. Un momento por favor...")
            plotter = ControllerPlotBestSellingProducts(PlotBestSellingProducts)
            plot = plotter.plot_best_selling_products(df, year, limited)
            plot.show()
            save_plot = input("¿Desea guardar el gráfico en un archivo? (s/n): ")
            if save_plot.lower() == 's' and plot is not None:
                print("Guardando gráfico en un archivo. Un momento por favor...")
                plotter.save_plot(plot, 'best_selling_products')
            else:
                pass
        else:
            return
        print("\n")
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        if controller is not None:
            controller.close()
from controllers.ControllerMostProfitableProducts import ControllerMostProfitableProducts
from controllers.ControllerPlotMostProfitableProducts import ControllerPlotMostProfitableProducts
from models.PlotMostProfitableProducts import PlotMostProfitableProducts

def ui_most_profitable_products(session):
    try:
        controller = ControllerMostProfitableProducts(session)
        print(r"""

.___  ___.      ___           _______.     _______      ___      .__   __.      ___      .__   __.   ______  __       ___      
|   \/   |     /   \         /       |    /  _____|    /   \     |  \ |  |     /   \     |  \ |  |  /      ||  |     /   \     
|  \  /  |    /  ^  \       |   (----`   |  |  __     /  ^  \    |   \|  |    /  ^  \    |   \|  | |  ,----'|  |    /  ^  \    
|  |\/|  |   /  /_\  \       \   \       |  | |_ |   /  /_\  \   |  . `  |   /  /_\  \   |  . `  | |  |     |  |   /  /_\  \   
|  |  |  |  /  _____  \  .----)   |      |  |__| |  /  _____  \  |  |\   |  /  _____  \  |  |\   | |  `----.|  |  /  _____  \  
|__|  |__| /__/     \__\ |_______/        \______| /__/     \__\ |__| \__| /__/     \__\ |__| \__|  \______||__| /__/     \__\ 
                                                                                                                               
                                                                                                                      
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
        df = controller.get_most_profitable_products(year, limit)
        
        if limit == None or limit > 20:
            print("Se guardará su reporte en un archivo Excel.")
            controller.save_to_excel(df, 'most_profitable_products')
        else:
            print(df)
            print("\n")
            save_to_excel = input("¿Desea guardar el reporte en un archivo Excel? (s/n): ")
            if save_to_excel.lower() == 's':
                print("Guardando reporte en un archivo Excel. Un momento por favor...")
                controller.save_to_excel(df, 'most_profitable_products')
            else:
                pass
        
        print("\n")
        show_plot = input("¿Desea ver un gráfico de los productos que generan más ganancia? (s/n): ")
        if show_plot.lower() == 's':
            limited = None
            if limit == None or limit > 10:
                limited = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 10): "))
            else:
                limited = limit
            print("Generando gráfico de productos que generan más ganancia. Un momento por favor...")
            plotter = ControllerPlotMostProfitableProducts(PlotMostProfitableProducts)
            plot = plotter.plot_most_profitable_products(df, year, limited)
            # Añadir validación de que el plot no sea None
            plot.show()
            save_plot = input("¿Desea guardar el gráfico en un archivo? (s/n): ")
            if save_plot.lower() == 's' and plot is not None:
                print("Guardando gráfico en un archivo. Un momento por favor...")
                plotter.save_plot(plot, 'most_profitable_products')
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
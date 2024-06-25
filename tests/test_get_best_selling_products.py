import pandas as pd
from controllers.ControllerBestSellingProducts import ControllerBestSellingProducts
from models.PlotBestSellingProducts import PlotBestSellingProducts

def test_get_best_selling_products(session):
    try:
        controller = ControllerBestSellingProducts(session)
        year = int(input("Ingrese el año a consultar: "))
        is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")
        
        if is_limited.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar: "))
        else:
            limit = None

        df = controller.get_best_selling_products(year, limit)

        if limit == None:
            print("Se guardará su reporte en un archivo Excel.")
            controller.save_to_excel(df, 'best_selling_products')
        else:
            print(df)
            save_to_excel = input("¿Desea guardar el reporte en un archivo Excel? (s/n): ")
            if save_to_excel.lower() == 's':
                controller.save_to_excel(df, 'best_selling_products')
            else:
                pass
            
        print("\n")
        show_plot = input("¿Desea mostrar el gráfico de tendencias trimestrales? (s/n): ")
        if show_plot.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar en el gráfico (Max: 20): "))
            plotter = PlotBestSellingProducts()
            plotter.plot_best_selling_products(df, year, limit)
        else:
            return
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        controller.close()
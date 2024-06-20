import pandas as pd
from matplotlib import pyplot as plt
from controllers.SalesReportController import SalesReportController

def test_get_best_selling_products():
    try:
        year = int(input("Ingrese el año a consultar: "))
        is_limited = input("¿Desea limitar el número de productos a mostrar? (s/n): ")

        if is_limited.lower() == 's':
            limit = int(input("Ingrese el número de productos a mostrar: "))
        else:
            limit = None

        controller = SalesReportController()
        df = controller.get_best_selling_products(year, limit)
        print(df)
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        controller.close()
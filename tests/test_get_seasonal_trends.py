import pandas as pd
from matplotlib import pyplot as plt
from controllers.SalesReportController import SalesReportController

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
        controller = SalesReportController()
        df = controller.get_seasonal_trends_by_quarter(year, quarter, limit)
        print(df)
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        if controller is not None:
            controller.close()
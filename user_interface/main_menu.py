import os
from user_interface.ui_seasonal_trends import ui_seasonal_trends
from user_interface.ui_best_selling_products import ui_best_selling_products
from user_interface.ui_most_profitable_products import ui_most_profitable_products
from user_interface.clear_util import clear
def main_menu(session):
    while True:
        print(r"""                                                                      
     _       _                 _                    __  __      _        _          
    / \   __| |_   _____ _ __ | |_ _   _ _ __ ___  |  \/  | ___| |_ _ __(_) ___ ___ 
   / _ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ | |\/| |/ _ \ __| '__| |/ __/ __|
  / ___ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ | |  | |  __/ |_| |  | | (__\__ \
 /_/   \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___| |_|  |_|\___|\__|_|  |_|\___|___/                                                                                                                                        
        """)
        print("\n")
        print("Bienvenido!")    
        print("\n")
        print("Por favor, seleccione una de las siguientes opciones:")
        print("1. Consultar tendencias estacionales")
        print("2. Consultar productos más vendidos")
        print("3. Consultar productos que generan más ganancia")
        print("4. Salir")
        print("\n")
        option = input("Ingrese el número de la opción deseada: ")
        if option == "1":
            clear()
            ui_seasonal_trends(session)
            clear()
        elif option == "2":
            clear()
            ui_best_selling_products(session)
            clear()
        elif option == "3":
            clear()
            ui_most_profitable_products(session)
            clear()
        elif option == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    

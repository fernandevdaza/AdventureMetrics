import os
from user_interface.ui_seasonal_trends import ui_seasonal_trends
from user_interface.ui_best_selling_products import ui_best_selling_products
from user_interface.ui_most_profitable_products import ui_most_profitable_products
def main_menu(session):
    while True:
        print(r"""
 ________  ________  ___      ___ _______   ________   _________  ___  ___  ________  _______           _____ ______   _______  _________  ________  ___  ________  ________      
|\   __  \|\   ___ \|\  \    /  /|\  ___ \ |\   ___  \|\___   ___\\  \|\  \|\   __  \|\  ___ \         |\   _ \  _   \|\  ___ \|\___   ___\\   __  \|\  \|\   ____\|\   ____\     
\ \  \|\  \ \  \_|\ \ \  \  /  / | \   __/|\ \  \\ \  \|___ \  \_\ \  \\\  \ \  \|\  \ \   __/|        \ \  \\\__\ \  \ \   __/\|___ \  \_\ \  \|\  \ \  \ \  \___|\ \  \___|_    
 \ \   __  \ \  \ \\ \ \  \/  / / \ \  \_|/_\ \  \\ \  \   \ \  \ \ \  \\\  \ \   _  _\ \  \_|/__       \ \  \\|__| \  \ \  \_|/__  \ \  \ \ \   _  _\ \  \ \  \    \ \_____  \   
  \ \  \ \  \ \  \_\\ \ \    / /   \ \  \_|\ \ \  \\ \  \   \ \  \ \ \  \\\  \ \  \\  \\ \  \_|\ \       \ \  \    \ \  \ \  \_|\ \  \ \  \ \ \  \\  \\ \  \ \  \____\|____|\  \  
   \ \__\ \__\ \_______\ \__/ /     \ \_______\ \__\\ \__\   \ \__\ \ \_______\ \__\\ _\\ \_______\       \ \__\    \ \__\ \_______\  \ \__\ \ \__\\ _\\ \__\ \_______\____\_\  \ 
    \|__|\|__|\|_______|\|__|/       \|_______|\|__| \|__|    \|__|  \|_______|\|__|\|__|\|_______|        \|__|     \|__|\|_______|   \|__|  \|__|\|__|\|__|\|_______|\_________\
                                                                                                                                                                       \|_________|                                                                                                                                                                                                                                                                                                                                                                   
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
        elif option == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
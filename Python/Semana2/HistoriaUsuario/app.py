""" 
    The program manages the inventory products by an Interactive main menu, 
    which controls the execution using a while loop with options from 1 to 4:
        option 1: create a product.
        option 2: show inventory
        option 3: calculate inventory statistics
        option 4: Ends execution using a break

        Each option calls its respective function, located in the 'functions' module.

"""

# It is imported from the functions module
from functions import create_product, show_inventory, calculate_statistics, clear_console


while True:

    # \n Newline
    # \t Tabulation
    print("\n\t**** Bienvenido a la gestión de productos del inventario ****")


    # The try/except block controls errors in the execution of the program
    try:

        option = int(input("\n 1) Agregar producto\n 2) Mostrar inventario\n 3) Calcular estadísticas\n 4) Salir\n\nIngrese el número de la opción que desea realizar: "))

        print()

        if option == 1:

            print("\n\t** Agregar productos al inventario **\n")
            create_product()

        elif option == 2:

            print("\n\t** Mostrar productos del inventario **\n")
            show_inventory()
            
        elif option == 3:
            
            print("\n\t** Estadísticas del inventario **")
            calculate_statistics()

        elif option == 4:
            
            print("\n\t*** Ha finalizado la ejecución del programa ***\n")
            break
        
        # If the number is not correct, raise an error.
        else: 
            raise ValueError


    # Catch the data type errors from the try block
    except:

        print("\n\t\t *** ¡Valor incorrecto! ***")
        print("\n\tDebe ser un número válido, Intente de nuevo.")
        print()

        clear_console(2)


    clear_console()

    
"""

Among the objectives for the week were:

    Understanding the characteristics and differences between Lists, Tuples, and Dictionaries. 
    Knowing when and how to use each of these data structures to organize and manage data in Python.
	
    Learning the basic syntax of For and While loops and understanding how they can be used to iterate over data structures.
	
    Using functions to modularize, organize, and reuse code.
    
    Finally, the aim was to integrate these concepts in the construction of simple programs and algorithms."
    
"""

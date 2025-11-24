"""
                  Main Module: Product Inventory Management (app)
    
    The program manages a product inventory using a main menu with different options controlled through a "While" loop.
    The loop options are:

        1) Add: Creates a new product by invoking the create_product function.
        2) Show: Shows all products in the inventory by invoking the show_inventory function.
        3) Search: Searches for a specific product by invoking the search_product function.
        4) Update: Updates a product using the search_product and update_product functions.
        5) Delete: Deletes a product using the search_product and delete_product functions.
        6) Statistics: Generates a summary of the main inventory statistics.
        7) Save CSV: Saves the inventory in CSV format by invoking the save_csv function.
        8) Load CSV: Loads the inventory from a CSV file by invoking the load_csv function.
        9) Exit: Terminates the program execution.

    The program is composed of three modules:
        
        * app (current module): Controls the menu and the program execution.
        * file: Contains the functions that control saving and loading the CSV file (save_csv, load_csv, delete_incorrect).
        * Services: Contains all the functions responsible for the CRUD (Create, Read, Update, Delete) operations 
        (create_product, show_inventory, search_product, update_product, delete_product, calculate_statistics).

"""


# The functions from the "services" module are imported
from services import create_product, show_inventory, search_product, update_product, delete_product, \
    calculate_statistics

# The functions from the "files" module are imported
from file import save_csv, load_csv, delete_incorrect, controlLoadCSV

# Path is imported from pathlib
from pathlib import Path

# Allows handling the absolute filePath of the folder and creates the inventory CSV file.
filePath = Path(__file__).parent / "inventory.csv"

inventory = []

# Inventory in memory 
# inventory = [{"name": "Cuaderno", "price": 100.2, "quantity": 10}, {"name": "Borrador", "price": 200.2, "quantity": 55}]

if filePath.exists():
    existsFile = True

else:
    existsFile = False 


# Main loop
while True:

    print("\n\t**** Bienvenido a la gestión de productos de inventario ****")

    # Try/except/else block that controls the menu options.
    try:
        option = int(input(
            "\n 1) Agregar\n 2) Mostrar\n 3) Buscar\n 4) Actualizar\n 5) Eliminar\n 6) Estadísticas\n 7) Guardar CSV \n 8) Cargar CSV \n 9) Salir"
                 "\n\nIngrese el número de la opción que desea realizar: "))

    except:

        print("\n\t** ¡Valor incorrecto, intente de nuevo! **")

    # If the "try" works, it goes into the "else".
    else:

        # "option" match
        match option:
        
            case 1:

                print("\n\t** Agregar productos al inventario **\n")

                # try/except/else that checks that the input data type is correct.
                try:
                    name = str(input("Ingrese el nombre: ")).capitalize()

                    price = float(input("Ingrese el precio: "))

                    quantity = int(input("Ingrese la cantidad: "))

                except:
                    print(
                        f"\n\t{" ":>6}** El tipo de dato ingresado es incorrecto **\n\t Recuerde que el precio y la cantidad deben ser números")


                # If the "try" works, it invokes the function "create_product".
                else:
                    inventory = create_product(inventory = inventory, name=name, price=price, quantity=quantity)

            case 2:
                
                try:

                    print("\n\t** Mostrar productos del inventario **\n")
                    show_inventory(inventory)

                except Exception as e:
                    print("\n\t¡Ha ocurrido un error!", e)

            case 3:

                try:
                    print("\n\t** Buscar productos del inventario **\n")

                    name = str(input("Ingrese el nombre: ")).capitalize()

                    searchProduct = search_product(inventory= inventory, name=name)

                    print(f"\n\t El resultado de la búsqueda es: {searchProduct}")

                except Exception as e:
                    print("\n\t¡Ha ocurrido un error!", e)


            case 4:

                # To update a product, first invoke the function "search_product", passing the inventory list as an argument to locate
                # the product within the inventory before proceeding with the update

                print("\n\t** Actualizar producto del inventario **\n")

                search = str(input("Ingrese el nombre del producto: ")).capitalize()
 
                result = search_product(inventory=inventory, name=search)

                # If it finds the product, the variable result returns a dictionary with it.
                # To verify this, isinstance is used
                if isinstance(result, dict):
                    
                    # The try/except/else controls the product update
                    try:

                        print(f"\n\tProducto encontrado: {result}")

                        # The variable arguments stores the arguments received by the function "update_product" in the form of a dictionary
                        arguments = {"inventory": inventory, "name": result}

                        # If the user accepts, the price and/or quantity is updated
                        updatePrice = str(input("\n¿Desea modificar el precio? (si/no): ")).lower()

                        # The updated values are added to the 'arguments' dictionary
                        if updatePrice == "si":

                            new_price = float(input("Ingrese el nuevo precio: "))

                            arguments["new_price"] = new_price

                        updateQuantity = str(input("\n¿Desea modificar la cantidad? (si/no): ")).lower()

                        if updateQuantity == "si":
                            new_quantity = int(input("Ingrese la nueva cantidad: "))

                            arguments["new_quantity"] = new_quantity

                    except:
                        print("Error")

                    # If the try founds, the else block invokes the function 'update_product'
                    # and unpacks the key-value pairs from the 'arguments' dictionary.
                    else:
                        inventory = update_product(**arguments)
                        
                # If isinstance doesn't find the dictionary, it returns a message that it didn't find the product.
                else:
                    print(result)

            case 5:
                
                # To delete the product, I first search using the "buscar_producto" function, which receives the
                # list of inventories and the product to search for
                
                print("\n\t** Eliminar productos del inventario **\n")

                search = str(input("Ingrese el nombre del producto: ")).capitalize()

                result = search_product(inventory=inventory, name=search)

                # If it finds the product, the "result" variable returns a dictionary of the product.
                # isinstance is used to verify this

                if isinstance(result, dict):
                    print(f"\n\tProducto encontrado: {result}")

                    delete = input("\n\tEstá seguro de eliminarlo? (si/no): ").lower()
                    
                    # The 'result' variable brings a key with the product's index in the inventory list.
                    if delete == "si":
                        delete_product(inventory=inventory, name = int(result["index"]))

                    else:
                        print("\n\tNo se ha eliminado el producto")
                        
                # If isinstance doesn't return the dictionary, it prints a message that it didn't find the product
                else:
                    print(result)
        

            case 6:
                try:
                    calculate_statistics(inventory)

                except:
                    print("\n\t ¡Error!, verifique que el inventario tenga productos")

        
            case 7:
                    
                                 
                    if inventory is None or len(inventory) == 0:

                        print("\n\t El inventario está vacío, no se puede guardar")

                    else:
                        if controlLoadCSV == False and existsFile == True:
                            print("\n\t¿Esta seguro que desea guarda un producto sin cargar el inventario?")
                            print("\n\tPuede generar productos duplicados, ¡Mejor cargue el CSV antes de guardar!")
                    
                        else:

                            try:
                                
                                # The 'controlLoadCSV' variable is used to prevent a CSV from being loaded again if another one has already been loaded previously
                                # It must be saved before loading again to avoid duplicating the inventory.
                                save_csv(inventory, filePath)
                                controlLoadCSV = False
                                firstSave = False

                            except:
                                print("\n\tNo se pudo guardar el archivo CSV")

                            else:
                                
                                # Empty the inventory list, so as not to duplicate products when the CSV is loaded
                                print("\n\t\tPara usar el inventario, cargue el archivo CSV")

                                inventory.clear()

            case 8:

                    # The "controlLoadCSV" variable prevents reloading the CSV without saving it first. Upon saving,
                    # the inventory list is freed to avoid duplicating values
                    if controlLoadCSV:
                       print("\n\t** Ya se había cargado un archivo CSV, guarde el inventario actual antes de cargar otra vez **")

                    else:

                        # If the cargar_csv function finds the CSV file in the filePath, it returns the "inventoryLoaded"
                        # and a boolean for the "incorrect" variable, which is True if it found invalid values or spaces in the CSV
                        try:
                            inventoryLoaded, incorrect = load_csv(filePath)
                            
                        except Exception as e:
                            print("\n\t¡El inventario no existe!, guarde un archivo CSV primero.")

                        else:

                            # If incorrect returns True, the delete_incorrect function is called with the file's filePath
                            if incorrect:
                                delete_incorrect(filePath, inventoryLoaded)
                                
                            # If the "inventoryLoaded" is a list, enter this condition
                            if isinstance(inventoryLoaded, list):

                                # The searchDuplicate loop compares the "inventory" variable, which is in memory,
                                # with the "inventoryLoaded" variable that comes from the CSV file,
                                # and then searches for repeated product names

                                searchDuplicate = True
                                            
                                while searchDuplicate:

                                    searchDuplicate = False

                                    # Iterate through two nested "for" loops: one in "inventory" and the other in "inventoryLoaded"
                                    for indexLoaded, productLoaded in enumerate(inventoryLoaded):
                                        for index, product in enumerate(inventory):
                                            
                                            # If it finds repetitions, it enters the condition
                                            if productLoaded["name"] == product["name"]:
                                                print(f"\n\t\t!El producto {productLoaded["name"]}, ya existe!")

                                                # It asks for an input to know what to do with the repetitions
                                                replace = int(input("\n 1) Reemplazar producto por lo cargado \n 2) Reemplazar producto por el actual"
                                                                   "\n 3) Cualquier otra tecla sumará la cantidad actual con lo cargado y conservará el precio actual"
                                                                   "\n\t¿Qué desea hacer?: "))

                                                match replace:
                                                    case 1:
                                                        product["price"] = productLoaded["price"]
                                                        product["quantity"] = productLoaded["quantity"]
                                                        inventoryLoaded.pop(indexLoaded)
                                                        print("\n\t¡Se ha reemplazado el producto correctamente!")

                                                    case 2:
                                                        inventoryLoaded.pop(indexLoaded)
                                                        print("\n\t¡Se ha reemplazado el producto correctamente!")

                                                    case _:
                                                        product["quantity"] += productLoaded["quantity"]
                                                        inventoryLoaded.pop(indexLoaded)
                                                        print("\n\t¡Se han sumado los productos correctamente!")
                                                
                                                # The variable "searchDuplicate" causes the "While" loop to iterate until no duplicate are found
                                                searchDuplicate = True

                                print("\n\t\tInventario cargado desde el CSV: \n")

                                for product in inventoryLoaded:
                                    for category in product:
                                        print(f"{category}: {product[category]}")
                                    print()

                                inventory.extend(inventoryLoaded)

                                controlLoadCSV = True

                                inventoryLoaded.clear()
                                
                                input("\n\tPresione una tecla para continuar...")


                                print("\n\t\tInventario total actual: \n")
                                
                                # Here, it already prints everything that is in the inventory after extending both lists
                                for product in inventory:
                                    for category in product:
                                        print(f"{category}: {product[category]}")
                                    print()

                                input("\n\tPresione una tecla para continuar...")

                            # If there is an error loading the CSV, the function 'load_csv' returns a message.
                            else:
                                print(inventoryLoaded)

            case 9:
                print("\n\t*** Ha finalizado la ejecución del programa ***\n")
                break

            # Any other option entered
            case _ :
                print("\n\t¡Valor incorrecto, intente de nuevo!")




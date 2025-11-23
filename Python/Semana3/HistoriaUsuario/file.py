"""
                    File Module: Product Inventory Management (file)

    This module contains the functions that allow saving and loading the CSV file with the inventory products. 

"""


# Import the functions DictReader and DictWriter from the csv module to read and write to CSV
from csv import DictReader, DictWriter

# From services, the categories list is imported.
from services import categories

# The variable controlLoadCSV prevents reloading the CSV without first saving it. 
# When saving, the inventory list is cleared/freed to avoid duplicating values
controlLoadCSV = False

def save_csv(inventory: list[dict], file_path, include_header: bool = True) -> None:

    """
    This function takes the inventory, the file path, and the include_header boolean and saves the inventory list to the path (file_path).

    Args:
        Inventory (list[dict]):  List of the dictionaries with the products
        file_path (str): CSV file path
        include_header (bool): include header or not in the CSV file

    Returns: 
        None

    """

    # Errors when saving the CSV are handled with the try/except/else block
    try:
                    
        with open(file_path, "+w", encoding='utf-8', newline="") as file:
                    
            # The 'DictWriter' function is passed the file and the column headers
            write = DictWriter(file, fieldnames=categories)

            # If the inventory is not empty, the rows are written to the CSV file
            if inventory is not None:
                try:

                    if include_header is True:
                        write.writeheader()
                    
                    write.writerows(inventory)

                except:
                    print("\t¡No se pudo guardar el inventario!")

            else:
                print("\n\t¡Error!, el inventario está vacío")

    except:
        print("\t¡No se pudo guardar el archivo!")

    else:
        print(f"\n\t¡Guardado con éxito!, la ruta es: {file_path}")


def load_csv(file_path, inventory: list[dict] = []) -> tuple[list[dict], bool]:

    """
    This function allows loading the saved inventory from the CSV file at the path (file_path).

    Args: 
        Inventory (list[dict]):  List of the dictionaries with the products
        file_path (str): CSV file path


    Returns:
        inventory (list[dict]):  List of the dictionaries with the products loaded
        incorrect (bool): True/False if you found incorrect columns in the CSV.

    """

    with open(file_path, "r", encoding="utf-8") as file:
        
        incorrect = False

        # Read the CSV with DictReader
        read = DictReader(file)

        # Count void rows
        void = 0

        if read is not None:
            columnsCSV = read.fieldnames
            
            # It gets the headers from the file 'read' and compares them with the 'categories' list, which contains ["name", "price", "quantity"].
            if columnsCSV != categories:
                    print("\n\t\t\t*** Columnas incorrectas ***")

                # If there are different headers, it iterates through them. If a column doesn't correspond, it prints it

                    for column in columnsCSV: # pyright: ignore[reportOptionalIterable]
                        if column not in categories:
                            print(f"\t\tColumna {column} no válida")

                    print(f"\n\tSolo se permiten las siguientes columnas:{categories}")

                    incorrect = True


            for row in read:
                void_row = 0
                product = {}

                for category in categories:

                    # Search for empty or null values in each key:value pair of the dictionary "row". 
                    # If found, the variable "void" takes the value of 1 and the loop stops
                    if row[category] is None or row[category] == "":
                        void_row = 1
                        break
                        
                    # f it finds no nulls or empty values, it saves the key:value pair of each product in the product dictionary, 
                    # transforming the data types to name:str, price:float, and quantity:int.
                    else:
                        if category == "name":
                            product[category] = str(row[category])

                        elif category  == "price":
                            product[category] = float(row[category])

                        elif category == "quantity":
                            product[category] = int(row[category])

                        else:
                            print("Error")

                # If there is no void_row in the product, add the dictionary to the inventory list
                if void_row == 0:
                    inventory.append(product)

                # If there are any, add the quantity of empties.
                else: void += void_row

        else:
            print("\n\tEl inventario está vacío")
    
    print(f"\n\t¡Se han cargado con éxito {len(inventory)} productos y {void} campo(s) vacio(s) omitido(s)!")
    return inventory, incorrect



def delete_incorrect(file_path, inventory: list[dict]) -> None:

    """
    This function allows the CSV file to be truncated, eliminating incorrect, empty, and invalid columns, 
    and then re-creating the CSV file with the correct information.

    Args: 
        file_path (str): CSV file path
        inventory (list[dict]): List of the dictionaries with the products

    Returns:
        None

    
    """
    incorrectColumns = input("\n\tDesea delete la columna incorrectas? (si/no):").lower()
    
    if incorrectColumns == "si":
        
        # The file's file_path has the unlink method applied to it, which deletes the file. 
        # The "save_csv" function is then invoked to save the file with the correct data.
        try:
            file_path.unlink(missing_ok=True)
            save_csv(inventory, file_path)

        except Exception as error:
            print("\n\tError, no se pudo delete las columnas incorrecta de la base de datos", error)

    else:
        print("\n\tNo se ha eliminado las columnas incorrecta de la base de datos")


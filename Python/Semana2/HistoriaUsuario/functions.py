"""
                Functions Module: Product Inventory Management (functions)

    This module provides the functions used in the app

        Functions:
            clear_console(type, seconds): Used to clear the console
            create_product(inventory, categories): Creates a new product
            show_inventory(inventory, categories): Displays the products in the inventory
            calculate_statistics(inventory, product): Calculates the statistics of the products in the inventory

"""

# The os and time modules are imported to execute Operating System commands and pause program execution, respectively.
from os import system
from time import sleep

# inventory = [{"name": "Lápiz", "price": 100, "quantity": 3}, {"name": "Borrador", "price": 80, "quantity": 5}]
inventory = []

# List with the categories to enter into the dictionary
categories = ["name", "price", "quantity"]


def clear_console(type: int = 1, seconds: int = 5) -> None:

    # The 'try' block is so that if the 'system("clear")' command fails, the program execution does not stop."
    if type == 1:
        
        try:
            # Clean the console
            system("clear")

        # Pass is used to avoid an error if it enters the except block.
        except:
            pass

    elif type == 2:

        # It stops the program execution for the time indicated by the variable seconds and clears the console
        try:
            sleep(seconds)
            system("clear")

        except:
            pass

    else:
        pass

def create_product(inventory: list[dict] = inventory, categories: list[str] = categories) -> None:

    product = {}

    # Initialization of validation variables for data types and checking if the product already exists in the inventory.
    exists = False
    incorrectType = False

    for category in categories:
        value = input(f"Ingrese {category} del product: ").capitalize()

        product[category] = value

    # try/except block to validate that the price and quantity inputs are numbers.
    try:
        float(product["price"])
        int(product["quantity"])
    
    except:
        incorrectType = True
        print("\n¡ERROR, El price y la quantity deben ser números!")


    # Loop that allows me to verify that a new product isn't in the inventory.
    for repeated in inventory:
        if repeated["name"] in product.values():
            print("\n\t¡El product ya existe!")
            exists = True

    # If the previous validations are correct, add the product dictionary to the inventory list.
    if not exists and not incorrectType:
        inventory.append(product)
        print("\n\t¡Se ha agregado con éxito!")
        
    clear_console(2, 2)


def show_inventory(inventory: list[dict] = inventory, categorias: list[str] = categories) -> None:

    if len(inventory)>0:

        for product in inventory:
            concatenate = ""

            # Loop that iterates through the categories list to concatenate the product's category and the product.
            for category in categorias:

                concatenate += f"{category}: {product[category]} | "

            # Print the variable concatenate from position 0 up to position -2 of the variable concatenate.
            print(concatenate[:-2])

        input(f"\n\n{" ":>2}Presione una tecla para continuar: ")

    else:
        print("\nEl inventory está vacío, primero debe ingresar algún product al inventory")
        
        clear_console(2, 4)



def calculate_statistics(inventory: list[dict] = inventory, product: dict = {}) -> None:

    statistics = int(input("\n 1) Valor total del inventory \n 2) La quantity total de productos registrados\n\nIngrese el número de la opción que desea realizar: "))

    addition = 0

    if len(inventory) == 0:

        print("\nEl inventory está vacío, primero debe ingresar algún product al inventory")

        clear_console(2)

    else:

        match statistics:
                
            case 1:    
                print("\n\t** Valor total del inventory **\n")

                for product in inventory:

                    # Multiply the price of each product by the quantity. Then, sum the values and assign the result to the variable addition.
                    addition += float(product["price"]) * float(product["quantity"])

                    print(f"""name: {product["name"]} | price: ${product["price"]} | calidad: {product["quantity"]} | valor total: ${float(product["price"])
                                                                                                                                      * float(product["quantity"]) :.2f}""")
                    # Print the total sum of the inventory with two decimals. (:.2f)
                print(f"\n\n* El valor total del inventory es ${addition:.2f}")

                    
            case 2:
                print("\n\t** Cantidad total de productos registrados **\n")

                productQuantity = len(inventory)

                for product in inventory:

                    # Sum the total quantity of the products in the inventory
                    addition += int(product["quantity"])
                        
                    print(f"name: {product["name"]} | price: {product["price"]} | quantity: {product["quantity"]}")

                print(f"\n\n* Hay {productQuantity} product(s) diferente(s) en el inventory")
                print(f"* En total hay una quantity de {addition} product(s)")

            case _:

                print("\n\t¡Valor incorrecto!, intente de nuevo")


        input(f"\n\n{" ":>2}Presione una tecla para continuar: ")
   
   

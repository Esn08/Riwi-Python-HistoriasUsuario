"""
                Services Module: Product Inventory Management (services)
        
        This module contains all the functions for performing the CRUD (Create, Read, Update, Delete) 
        and calculating the program's statistics.
"""


# List with the keys that the products need
categories = ["name", "price", "quantity"]


def create_product(name: str, price: float, quantity: int, inventory: list[dict] = []) -> list[dict]:

    """
    This functions add a new product to inventary

    Args: 
        name (str): New product name
        price (float): New product price
        quantity (int): New product quantity
        inventory (list[dict]): Products list

    Returns:
        inventory (list[dict]):  Inventary with a new product
    """

    # If a repeated value is found, saving is not allowed. It returns the inventory unmodified
    for repeated in inventory:
        if repeated["name"] == name:
            print("\n\tEl producto ya existe en el inventario, ingrese otro o actualice el producto actual.")

    # If a repeated product isn't found, the product dictionary is created, 
    # it's added to the inventory list, and the list is returned

    else:
        product = {"name": name, "price": price, "quantity": quantity}
        inventory.append(product)
        print(f"\n\t ¡Se ha agregado con éxito el producto {name} al inventario!")

    return inventory

def show_inventory(inventory: list[dict] = []) -> None:

    
    """
    This functions print all products within inventory
    
    Args: 
        inventory (list[dict]): Products list

    Returns:
        None
    """

    if len(inventory) == 0:
        print("\n¡No existen datos en el inventario!, ingrese un producto primero o cargue el CSV")

    else:
        for product in inventory:
            for category in categories:
                print(f"{category}: {product[category]}")
            print()

    input(f"\n{" ":<3}Presione una tecla para continuar...")


def search_product( name: str, inventory: list[dict] = []) -> dict[str, float] | str:

    """
    This functions search a product within inventary

    Args: 
        name (str): Product name to search
        inventory (list[dict]): Products list

    Returns:
        productFound (dict): Product searched
    """


    if len(inventory) == 0:
        return "\n¡No existen datos en el inventario!, ingrese un producto primero"

    else:

        # Iterate over the for loop in the inventory list and enumerate the position
        for index, product in enumerate(inventory):

            # If the product name is in the inventory. Create a dictionary called "productFound", add the product's data to the dictionary, 
            # including the index position in the inventory list, and return it.
            if name == product["name"]:
                productFound  = {"name": product["name"], "price": product["price"], "quantity":
                    product["quantity"], "index": index}

                return productFound

        else:
            return "\n\n\t\t ¡El producto no se encontró!"


def update_product(name: dict, new_price: float | None = None, new_quantity: float | None = None, inventory: list[dict] = []) -> list[dict]:

    """
    This function update a product within inventory
    
    Args: 
        name (dict): Dictionary with the found product
        new_price (float | None): A number with the new price or None 
        new_quantity (float | None): A number with the new quantity or None 
        inventory (list[dict]): Products list

    Returns:
        inventory (list[dict]): Inventory list updated
    """


    if new_price is None and new_quantity is None:
        print("\n\t ¡No se ha actualizado el producto!")

    else:
        
        # The variable 'name' is a dictionary with the data returned by the function 'search_product'.
        product = {"name": name ["name"]}

        if new_price is not None:

            product["price"] = new_price

        if new_quantity is not None:
            product["quantity"] = new_quantity

        # The "name" has a key called index with the position of that product in the list. 
        # The product dictionary is updated at the same index position in the inventory list
        inventory[name["index"]] = product

        print("\n\t ¡Se ha actualizado el producto correctamente!")

    return inventory


def delete_product(name: int, inventory: list[dict] = []) -> None:

    """
    This function delete a product within inventory
    
    Args: 
        name (dict): Dictionary with the found product 
        inventory (list[dict]): Products list

    Returns:
        None
    """

    try:
        inventory.pop(name)

    except:
        print("\n\t¡No se pudo eliminar el producto!")

    else:
        print("\n\t\t¡Eliminado con éxito!")


def calculate_statistics(inventory: list[dict]) -> None:

    """
    This function generates a summary of the main inventory statistics.

    Args: 
        inventory (list[dict]): Products list

    Returns:
        None
    """

    sumQuantity = 0
    totalValue = 0

    for product in inventory:

        # The quantities are added
        sumQuantity += product["quantity"]

        # A lambda function is applied where each product dictionary is passed as an argument, and the "price" and "quantity" keys are accessed. 
        # Quantity * price is multiplied for each product and the result is summed into "totalValue"
        value = lambda p: p["quantity"] * p["price"]
        totalValue += value(product)

    # The maximum is calculated with the $\text{max}$ function, and in the "key" parameter, a lambda function is passed to sort by that key:value
    maxQuantity = max(inventory, key=lambda x: x["quantity"])
    maxPrice = max(inventory, key=lambda x: x["price"])

    print("\n\t\t*** Estadísticas del inventario ***")
    print("\n\tLas unidades totales son:", sumQuantity)
    print("\tEl valor total es:", "$", round(totalValue, 2))
    print(f"\n\tEl producto más caro es: {maxPrice["name"]}, precio: {maxPrice["price"]:.2f}")
    print(f"\tEl producto con más stock es: {maxQuantity["name"]}, cantidad: {maxQuantity["quantity"]}")

    input(f"\n{" ":<3}Presione una tecla para continuar...")

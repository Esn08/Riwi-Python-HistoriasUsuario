# Lista con las claves que necesitan los productos
categorias = ["name", "price", "quantity"]


def agregar_producto(inventario: list[dict], nombre: str, precio: float, cantidad: int) -> list[dict] | None:

    # Recorre un bucle del inventory
    # Si encuentra un valor repetido no permite guardar. Retorna el inventory sin modificar
    for repetido in inventario:
        if repetido["name"] == nombre:
            print("\n\tEl product ya existe en el inventory, ingrese otro o actualice el product actual.")

            return inventario

        # Si no encuentra un product repetido, se crea el diccionario product
        # lo agrega a la lista inventory y retorna la lista
        else:
            producto = {"name": nombre, "price": precio, "quantity": cantidad}

            inventario.append(producto)
            print(f"\n\t ¡Se ha agregado con éxito el product {nombre} al inventory!")

            return inventario

    return None


def mostrar_inventario(inventario: list[dict]) -> None:

    if len(inventario) == 0:
        print("\n¡No existen datos en el inventory!, ingrese un product primero")

    else:
        for producto in inventario:
            for categoria in categorias:
                print(f"{categoria}: {producto[categoria]}")
            print()

    input(f"\n{" ":<3}Presione una tecla para continuar...")


def buscar_producto(inventario: list[dict], nombre: str) -> str | dict:

    if len(inventario) == 0:
        return "\n¡No existen datos en el inventory!, ingrese un product primero"

    else:

        # Recorre bucle for en la lista inventory y enumera la posición
        for indice, producto in enumerate(inventario):

            # Si el name del product está en el inventory. Crea un diccionario llamado "productoEncontrado"
            # Se agrega los datos del product al diccionario, incluyendo la posición índice en la lista inventory y lo retorna
            if nombre == producto["name"]:
                productoEncontrado = {"name": producto["name"], "price": producto["price"], "quantity":
                    producto["quantity"], "indice": indice}

                return productoEncontrado

        else:
            return "\n\t ¡El product no se encontró!"


def actualizar_producto(inventario: list[dict], nombre: dict, nuevo_precio: float | None = None, nueva_cantidad: float | None = None) -> list[dict]:

    # Se verifica que el parámetro nuevo_precio o nueva_cantidad no sea None
    if nuevo_precio is None and nueva_cantidad is None:
        print("\n\t ¡No se ha actualizado el product!")

    else:

        # Se verifica que el parámetro nuevo_precio o nueva_cantidad no sea None
        if nuevo_precio is not None:

            # La variable, "name" es un diccionario con los datos
            # Que retornó la función "buscar_producto"
            nombre["price"] = nuevo_precio

        if nueva_cantidad is not None:
            nombre["quantity"] = nueva_cantidad

        # El diccionario "name" tiene una clave llamada índice con la posición de ese product en la lista
        # Se actualiza el diccionario product en la misma posición del índice en la lista inventory
        inventario[nombre["indice"]] = nombre

        print("\n\t ¡Se ha actualizado el product correctamente!")

    return inventario


def eliminar_producto(inventario: list[dict], nombre: int) -> None:

    # La variable "name" recibe el número del índice en que se encuentra el product a eliminar en la lista inventory
    try:
        inventario.pop(nombre)

    except:
        print("\n\tNo se pudo eliminar el product")

    else:
        print("\n\t¡Eliminado con éxito!")


def calcular_estadisticas(inventario: list[dict]) -> None:
    sumaCantidad = 0
    valorTotal = 0
    cantidad = {}
    precio = {}

    # Se recorre la lista inventory en un bucle, donde la variable product es cada diccionario con el product
    for producto in inventario:
        # Se suman las cantidades
        sumaCantidad += producto["quantity"]

        # Se aplica una función lambda donde se pasa como argumento cada diccionario product y se accede a las claves price y quantity
        # Se multiplica quantity * price en cada product y se suma en valorTotal
        valor = lambda p: p["quantity"] * p["price"]
        valorTotal += valor(producto)

    # Se calcula el máximo con la función max y en el parámetro "key" se pasa una función lambda para ordenar por esa clave:valor
    maxCantidad = max(inventario, key=lambda x: x["quantity"])
    maxPrecio = max(inventario, key=lambda x: x["price"])

    print("\n\t\t*** Estadísticas del inventory ***")
    print("\n\tLas unidades totales son:", sumaCantidad)
    print("\tEl valor total es:", "$", valorTotal)
    print(f"\n\tEl product más caro es: {maxPrecio["name"]}, price: {maxPrecio["price"]}")
    print(f"\tEl product con más stock es: {maxCantidad["name"]}, quantity: {maxCantidad["quantity"]}")

    input(f"\n{" ":<3}Presione una tecla para continuar...")

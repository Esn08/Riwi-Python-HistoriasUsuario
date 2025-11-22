# Se importan las funciones del módulo servicios
from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, \
    calcular_estadisticas

# Se importan las funciones del módulo archivos
from archivos import guardar_csv, cargar_csv, eliminar_incorrectos, manejoCargaCSV

# Se importa Path desde pathlib
from pathlib import Path

# Me permite manejar la ruta relativa de la ubicación de mi carpeta y crea el archivo CSV inventory
ruta = Path(__file__).parent / "inventory.csv"

# inventory = []

# Inventario en memoria 
inventario = [{"name": "Cuaderno", "price": 100.2, "quantity": 10},
               {"name": "Marcadores", "price": 200.2, "quantity": 55}
              ]

# Bucle que controla el menú
while True:

    print("\n\t**** Bienvenido a la gestión de productos de inventory ****")

    # Bloque try/except/else que controla las opciones del menú
    try:
        opcion = int(input(
            "\n 1) Agregar\n 2) Mostrar\n 3) Buscar\n 4) Actualizar\n 5) Eliminar\n 6) Estadísticas\n 7) Guardar CSV \n 8) Cargar CSV \n 9) Salir"
                 "\n\nIngrese el número de la opción que desea realizar: "))

    except:

        print("\n\t** ¡Valor incorrecto, intente de nuevo! **")

    # Si el try funciona ingresa al else
    else:

        # Match de la variable "option"
        match opcion:
        
            case 1:

                print("\n\t** Agregar productos al inventory **\n")

                # try/except/else que controla que el type de dato ingresado sea correcto
                try:
                    nombre = str(input("Ingrese el name: ")).capitalize()

                    precio = float(input("Ingrese el price: "))

                    cantidad = int(input("Ingrese la quantity: "))

                except:
                    print(
                        "\n El type de dato ingresado es incorrecto\n Recuerde que el price y la quantity deben ser números")
                    
                
                # Si el try funciona invoca la función "agregar_producto"
                else:
                    inventario = agregar_producto(inventario, nombre=nombre, precio=precio, cantidad=cantidad)

            case 2:

                print("\n\t** Mostrar productos del inventory **\n")
                mostrar_inventario(inventario)

            case 3:

                print("\n\t** Buscar productos del inventory **\n")

                nombre = str(input("Ingrese el name: ")).capitalize()

                busquedaProducto = buscar_producto(inventario, nombre=nombre)

                print(f"\n\t El resultado de la búsqueda es: {busquedaProducto}")

            case 4:

                # Para actualizar product primero busco con la función "buscar_producto" que recibe la lista de inventarios
                # y el product que voy a buscar

                print("\n\t** Actualizar product del inventory **\n")

                buscar = str(input("Ingrese el name del product: ")).capitalize()

                resultado = buscar_producto(inventario, nombre=buscar)

                # Si encuentra el product, la variable resultado me arroja un diccionario del product,
                # Para verificar esto se usa isinstance
                if isinstance(resultado, dict):
                    
                    # El try/except/else controla la actualización del product
                    try:

                        print(f"\n\tProducto encontrado: {resultado}")

                        # la variable argumentos almacena en forma de diccionario los argumentos que recibe la función "actualizar_producto"
                        argumentos = {"inventory": inventario, "name": resultado}

                        # Si el usuario acepta, se actualiza el price y/o la quantity.
                        actualizarPrecio = str(input("\n¿Desea modificar el price? (si/no): ")).lower()

                        # Se agrega al diccionario "argumentos" los valores actualizados.
                        if actualizarPrecio == "si":

                            nuevo_precio = float(input("Ingrese el nuevo price: "))

                            argumentos["nuevo_precio"] = nuevo_precio

                        actualizarCantidad = str(input("\n¿Desea modificar la quantity? (si/no): ")).lower()

                        if actualizarCantidad == "si":
                            nueva_cantidad = int(input("Ingrese la nueva quantity: "))

                            argumentos["nueva_cantidad"] = nueva_cantidad

                    except:
                        print("Error")

                    # Si el try funciona, else invoca la función "actualizar_producto" y desempaqueta
                    # la "clave:valor" del diccionario "argumentos"
                    else:
                        inventario = actualizar_producto(**argumentos)
                        
                # Si isinstance no encuentra el diccionario, trae un mensaje de que no encontró el product
                else:
                    print(resultado)

            case 5:
                
                # Para eliminar el product primero busco con la función "buscar_producto", recibe la lista de inventarios y el product que voy a buscar
                
                print("\n\t** Eliminar product del inventory **\n")

                buscar = str(input("Ingrese el name del product: ")).capitalize()

                resultado = buscar_producto(inventario, nombre=buscar)

                # Si encuentra el product, la variable "resultado" arroja un diccionario del product
                # Para verificar esto se usa isinstance
                if isinstance(resultado, dict):
                    print(f"\n\tProducto encontrado: {resultado}")

                    # Si "buscar_producto" encuentra el product, se confirma la eliminación
                    eliminar = input("\n\tEstá seguro de eliminarlo? (si/no): ").lower()
                    
                    # La variable resultado trae una clave con el índice del product en la lista inventory
                    if eliminar == "si":
                        eliminar_producto(inventario, nombre = resultado["indice"])

                    else:
                        print("\n\tNo se ha eliminado el product")
                        
                # Si isinstance no devuelve el diccionario, imprime un mensaje de que no encontró el product
                else:
                    print(resultado)
        

            case 6:
                calcular_estadisticas(inventario)

        
            case 7:
                
                # Para guardar en CSV, comprueba que el inventory no esté vacío
                if inventario is None or inventario == []:

                    print("\n\t El inventory está vacío no se puede guardar")

                # Si no está vacío invoca a la función "guardar_csv", que recibe el inventory y la ruta donde guardar
                else:
                    
                    try:
                        
                        # La variable manejoCargaCSV, se usa para evitar que se pueda cargar un CSV de nuevo, si ya se cargó otro previamente. 
                        # Se debe guardar antes de volver a cargar, para no duplicar el inventory
                        guardar_csv(inventario, ruta)
                        manejoCargaCSV = False

                    except:
                        print("\n\tNo se pudo guardar el archivo CSV")

                    else:
                        
                        # Vacíar la lista inventory, para no duplicar productos cuando se carga el CSV
                        inventario = []
                        print("\n\t\tPara usar el inventory, cargue el archivo CSV")


            case 8:
                    # La variable manejoCargaCSV, impide volver a cargar el CSV sin guardarlo antes, 
                    # Al guardar se libera la lista inventory para no duplicar valores
                    if manejoCargaCSV:
                       print("\n\t** Ya se había cargado un archivo CSV, guarde el inventory actual antes de cargar otra vez **")

                    else:
                        
                        # Si la función "cargar_csv" encuentra en la ruta el archivo CSV
                        # Retorna el "inventarioCargado", y un booleano para la variable "incorrectos", True si encontro valores inválidos o espacios en el CSV
                        try:
                            inventarioCargado, incorrectos = cargar_csv(ruta=ruta)

                        except Exception as e:
                            print("\n\t¡El inventory no existe!, guarde un archivo CSV primero.", e)

                        else:
                            
                            # Si incorrectos retorna True se llama a la función "eliminar_incorrectos" con la ruta del archivo
                            if incorrectos:
                                eliminar_incorrectos(ruta)
                                
                            # Si el "inventarioCargado" es una lista, ingresa a esta condición
                            if isinstance(inventarioCargado, list):

                                # El bucle buscarRepetidos compara la variable "inventory" que está en memoria
                                # Con la variable "inventarioCargado" que viene del CSV
                                # En busca de nombres de product repetidos
                                
                                buscarRepetidos = True
                                            
                                while buscarRepetidos:

                                    buscarRepetidos = False

                                    # Recorre dos bucles "for" anidados uno en "inventory" otro en "inventarioCargado"
                                    for posicionCargado, productoCargado in enumerate(inventarioCargado):
                                        for posicion, producto in enumerate(inventario):
                                            
                                            # Si encuentra repetidos, entra a la condición
                                            if productoCargado["name"] == producto["name"]:
                                                print(f"\n\t\t!El product {productoCargado["name"]}, ya existe!")

                                                # Pide un input para saber que hacer con los repetidos
                                                reemplazar = int(input("\n 1) Reemplazar product por lo cargado \n 2) Reemplazar product por el actual"
                                                                   "\n 3) Cualquier otra tecla sumará el price y quantity actual con lo cargado "
                                                                   "\n\t¿Qué desea hacer?: "))

                                                # De acuerdo a la opción reemplaza por el valor de quantity y price,
                                                # Deja el actual o suma ambos valores
                                                match reemplazar:
                                                    case 1:
                                                        producto["price"] = productoCargado["price"]
                                                        producto["quantity"] = productoCargado["quantity"]
                                                        inventarioCargado.pop(posicionCargado)
                                                        print("\n\t¡Se ha reemplazado el product correctamente!")

                                                    case 2:
                                                        inventarioCargado.pop(posicionCargado)
                                                        print("\n\t¡Se ha reemplazado el product correctamente!")

                                                    case _:
                                                        producto["price"] += productoCargado["price"]
                                                        producto["quantity"] += productoCargado["quantity"]
                                                        inventarioCargado.pop(posicionCargado)
                                                        print("\n\t¡Se han sumado los productos correctamente!")
                                                
                                                # La variable "buscarRepetidos" hace que el bucle "While" se recorra hasta que no encuentre repetidos
                                                buscarRepetidos = True

                                print("\n\t\tInventario cargado desde el CSV: \n")

                                # Acá, recorre dos bucles "for" anidados en el "inventarioCargado" desde CSV
                                # Recorre las categories de cada product e imprime todos los productos cargados del CSV

                                for producto in inventarioCargado:
                                    for categoria in producto:
                                        print(f"{categoria}: {producto[categoria]}")
                                    print()

                                # A la lista en memoria "inventory" se le extiende "inventarioCargado"
                                inventario.extend(inventarioCargado)

                                manejoCargaCSV = True
                                
                                # Detiene la ejecución del programa para ver el inventarioCargado
                                input("\n\tPresione una tecla para continuar...")

                                
                                print("\n\t\tInventario total actual: \n")
                                
                                # Acá, ya imprime todo lo que hay en el inventory después de extender ambas listas
                                for producto in inventario:
                                    for categoria in producto:
                                        print(f"{categoria}: {producto[categoria]}")
                                    print()

                                # Detiene la ejecución del programa para ver el inventory
                                input("\n\tPresione una tecla para continuar...")

                            # Si hay error al cargar el CSV, la función "cargar_csv" retorna un mensaje.
                            else:
                                print(inventarioCargado)

            # Fin del bucle.
            case 9:
                print("\n\t*** Ha finalizado la ejecución del programa ***\n")
                break
                
            # Cualquier otra opción ingresada
            case _ :
                print("\n\t¡Valor incorrecto, intente de nuevo!")




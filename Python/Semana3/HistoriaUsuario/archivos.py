# Importar del módulo csv las funciones DictReader, DictWriter para leer y escribir en CSV
from csv import DictReader, DictWriter

# De servicios importa la lista categories
from servicios import categorias

# La variable manejoCargaCSV, impide volver a cargar el CSV sin guardarlo antes, 
# Al guardar se libera la lista inventory para no duplicar valores
manejoCargaCSV = False

def guardar_csv(inventario: list[dict], ruta: str, incluir_header: bool = True) -> None:

    # Con el bloque try/except/else se manejan los errores al guardar el CSV
    try:
        with open(ruta, "w", encoding='utf-8', newline= "") as archivo:
            
            # A la función "DictWriter" se le pasa el archivo y los encabezados de la columna
            escribir = DictWriter(archivo, fieldnames=categorias)

            # Si el parámetro "incluir_header" es True, se escribe en el archivo CSV el encabezado
            if incluir_header:
                escribir.writeheader()

            # Si el inventory no está vacío, se escriben las filas en el archivo CSV
            if inventario is not None:
                try:
                    escribir.writerows(inventario)

                except:
                    print("No se pudo guardar el inventory")

            else:
                print("\n\t¡Error!, el inventory está vacío")
    except:
        print("No se pudo guardar el archivo")

    else:
        print(f"\n\t¡Guardado con éxito!, la ruta es: {ruta}")

    return None



def cargar_csv(ruta: str, inventario: None = None) -> tuple[list[dict], bool]:

    
    if inventario is None:
        inventario = []

    with open(ruta, "r", encoding="utf-8") as archivo:
        
        incorrectos = False

        # Lee el CSV con DictReader
        leer = DictReader(archivo)

        # Si leer existe
        if leer is not None:

            # Trae las encabezados del archivo "leer" y los compara con la lista "categories" que tiene ["name", "price", "quantity"]
            if list(leer.fieldnames) != categorias:
                    print("\n\t\t\t*** Columnas incorrectas ***")

                # Si hay encabezados diferentes, los recorre. Si una columna no corresponde, la imprime
                    for indice, columna in enumerate(leer.fieldnames):
                        if columna not in categorias:
                            print(f"\t\tColumna {columna} no válida")

                    print(f"\n\tSolo se permiten las siguientes columnas:{categorias}")

                    # Se inicializa la varible incorrectos
                    incorrectos = True

            # Cuenta filas vacias
            vacias = 0

            # Recorre la lista "leer"
            for fila in leer:
                vacia = 0
                producto = {}

                # Recorre la lista "categories"
                for categoria in categorias:

                    # Busca vacíos o nulos en cada clave:valor del diccionario "fila"
                    # Si encuentra, la variable "vacia" toma el valor de 1 y se detine el bucle
                    if fila[categoria] is None or fila[categoria] == "":
                        vacia = 1
                        break
                        
                    # Si no encuentra nulos o vacios, guarda en el diccionario product la clave:valor de cada product.
                    # Transformando el type de dato =  name:str, price:float y quantity:int
                    else:
                        if categoria == "name":
                            producto[categoria] = str(fila[categoria])

                        elif categoria  == "price":
                            producto[categoria] = float(fila[categoria])

                        elif categoria == "quantity":
                            producto[categoria] = int(fila[categoria])

                        else:
                            print("Error")

                # Si no hay vacios en el product, agrega el diccionario a la lista "inventory"
                if vacia == 0:
                    inventario.append(producto)

                # Si no, suma la quantity de vacíos
                else: vacias += vacia

        else:
            print("\n\tEl inventory está vacío")
    
    print(f"\n\t¡Se han cargado con éxito {len(inventario)} productos y {vacias} campo(s) vacio(s) omitido(s)!")
    return inventario, incorrectos


# Si al intentar cargar el CSV se encuentran errores o columnas que no son, se invoca esta función
def eliminar_incorrectos(ruta: str) -> None:
    columnasIncorrectas = input("\n\tDesea eliminar la columna incorrectas? (si/no):").lower()
    
    # Si "columnasIncorrectas" 
    if columnasIncorrectas == "si":
        
        # A la ruta del archivo le aplica el método unlink que lo elimina.
        # Se invoca "guardar_csv" para guardar el archivo con los datos correctos.
        try:
            ruta.unlink(missing_ok=True)
            guardar_csv(inventario, ruta)
            

        except Exception as error:
            print("\n\tError, no se pudo eliminar las columnas incorrecta de la base de datos", error)

    
    else:
        print("\n\tNo se ha eliminado las columnas incorrecta de la base de datos")


""" 

    The program requests three inputs from the console: name, quantity, and price. It verifies if the entered data are of the correct data type. 
    If the condition is met and the data are correct, it calculates the total cost (quantity * price) and prints a message on the screen with the product information

"""


# system and sleep are imported from the "os" and "time" libraries.
from os import system
from time import sleep


while True:
    
    # A try/except block that allows for error handling if the entered data type is incorrect.
    try:

        name = str(input("\nDigite el nombre del product: ").capitalize())
        quantity = int(input("Digite la cantidad (Debe ser un número entero): "))
        price = float(input("Digite el precio (Debe ser un número): "))

    except:
        
        print("\n\t\t¡Ha ocurrido un error!\n")
        print("El valor ingresado de 'Cantidad' y/o 'Precio' no es correcto")
        print("\t\t¡Intente de nuevo!")
        
        try:
            # A function that pauses (or stops) the program's execution for 6 seconds.
            sleep(6)
            
            # A function that allows the Linux console to be cleared using the 'clear' command.
            system("clear")

        # If 'clear' does not work, the program should not stop its execution.
        except:
            pass
        
    # The else block is executed only if the try block works correctly.
    else:
        
        total_cost = (quantity * price)

        # '\n': Newline (or line break) 
        # '\t': Tabulation (or tab) 
        # :.2f: Rounds the number to two decimal places.
        print(f"\n\t{"*"*5} Nombre del product: {name}, Cantidad: {quantity} | Precio: ${price:.2f} | Costo Total: ${total_cost:.2f} {"*" * 5}\n")
        break
        


'''
crear una funcion llamada menu()
parametros de entrada : ninguno
lo que realiza : muestra un menu y pide al usuarioque selecione una opcion
valor de retorno : la opcion seleccionada 
'''

def menu():
    print("1. entradas\n2. platos fuertes\n3. bebidas\n4. postres\n5. salir")
    opcion = int(input("elija una opcion: "))
    return opcion
def entradas():
    print("1. pan de bono\t\t$3000")
    print("2. empanadas\t\t$2500")
def fuertes():
    print("1.pollo apanado\t\t$30000")
    print("2. salchipapa\t\t$10000")
    print("3. hamburguesa\t\t$25000")
def bebidas():
    print("1. gaseosas\t\t$5000")
    print("2. limonada\t\t$4000")
    print("3.cerveza\t\t$5000")
def postres():
    print("1.waflees\t\t$15000")
    print("2. postre de milo\t\t$7000")


#funcion principal
def main():
    eleccion = menu()
    print(eleccion)

    match (eleccion):
        case 1:
            entradas()
        case 2:
            fuertes()
        case 3:
            bebidas()
        case 4:
            postres()
        case _:
            print("opcion no valida")
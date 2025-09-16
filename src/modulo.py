'''
import mod_funciones2
 
#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
mod_funciones2.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
mod_funciones2.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
mod_funciones2.tabla(multiplicando)
'''
'''
from mod_funciones2 import *

primo (9)
tabla (77)
fibonacci (79)

'''
from mod_funciones2 import *
def main():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                print ("calcular si un numero es primo ")
                valor = int (input("ingrese un numero mayor que uno"))
                primo (valor)
            case 2:
                print ("tabla de multiplicar ")
                numero = int (input("ingrese el nuemro"))
                tabla(numero)
            case 3:
                print ("serie de fibonacci")
                numero = int(input("ingresa el numero de terminos"))
                fibonacci(numero)
            case 4:
                break
            case _:
                print ("la opcion no es valida ")


if __name__ == "__main__":
    main()

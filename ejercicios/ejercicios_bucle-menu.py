### jercicio 1: Conversor de Temperatura
'''
Crea un programa que convierta temperaturas entre Celsius y Fahrenheit. El programa debe:
1. Preguntar al usuario si desea convertir de Celsius a Fahrenheit (ingresando 'C') o de Fahrenheit a Celsius (ingresando 'F')
2. Aceptar un valor de temperatura como entrada
3. Realizar la conversión usando la fórmula apropiada
4. Continuar pidiendo conversiones hasta que el usuario ingrese 'Q' para salir
'''
'''
variable de entrada:
nombre          tipo
opcion          str
temperatura     float

Variable de salida:
nombre          tipo
conversion      float

Variable de control
opcion
'''
'''
opcion = 'Z'
while opcion != 'Q':
    opcion = input("F. Fahrenheit a Celsius\nC. Celsius a Fahrenheit\nQ. salir\n").upper()
    if opcion != 'Q':
        temperatura = float(input("ingrese la temperatura a convertir: "))
        match opcion:
            case 'F':
                conversion = (temperatura - 32)* (5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case 'C':
                conversion = (temperatura * 9/5) + 32
                print(f"{temperatura}°C = {conversion}°F ")
            case _:
                print("opcion no valida")
    else:
        print("saliendo del programa")
'''
'''
numero = int(input("ingrese un numero entero mayor que 1: "))
cont = 0
for i in range(1,numero + 1):
    if numero % i == 0:
        cont += 1 
if cont == 2:
    print(f"{numero} es primo")
else:
    print(f"los divisores de {numero} son") 
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
'''


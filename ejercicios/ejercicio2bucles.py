## serie de fibonaci
'''

# Solicitar al usuario un número entero
Imprimir("Ingrese un número entero para generar la serie de Fibonacci:")
Leer(num)

# Verificar si el número ingresado es válido
Si num <= 0, entonces:
    Imprimir("Por favor, ingrese un número entero positivo.")
Sino si num == 1, entonces:
    Imprimir("Serie de Fibonacci:")
    Imprimir(0)
Sino:
    # Inicializar los primeros dos términos de la serie
    a = 0
    b = 1
    contador = 2  # Iniciar en 2 debido a los dos primeros términos ya impresos

    # Imprimir los primeros dos términos
    Imprimir("Serie de Fibonacci:")
    Imprimir(a)
    Imprimir(b)

    # Calcular e imprimir los términos restantes
    Mientras contador < num, hacer:
        siguiente = a + b
        Imprimir(siguiente)
        a = b
        b = siguiente
        contador += 1
'''
## trancripcion a python
'''
numero = int(input("ingrese el numero de terminos de la serie : "))
if numero <= 0:
    print("por favor, ingrese un numero entero positivo.")
elif numero == 1:
    print("serie de fibonaci")
    print(0)
else:
    a = 0
    b = 1
    contador = 2 
    print("serie de fibonaci")
    print(a)
    print(b)

    while contador < numero: 
        siguiente = a + b
        print(siguiente)
        a = b 
        b = siguiente
        contador += 1

'''

# tabal de multiplicar 5
'''
numero = int(input("ingrese un numero entero: "))
print(f"tabla de multiplicar de {numero}: ")
i = 1
while i <= 15:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
'''
## ejercicio con bucle for 
'''
for cont in range (-20, 0, 1):
    print(cont)
'''
'''
n = int(input("ingrese el numero al que va llegar el rango: "))
while n < 0:
    n = int(input("ingrese el numero al que va llegar el rango: "))
acum = 0
for cont in range (1, n+1):
    print(cont)
    if cont % 2 == 0:
        acum += cont
print(f"la suma de los numero pares es :{acum} ")

'''
mensaje  = " universidad pontificia bolivariana"
numero = int(input("ingrese un numero entero positivo: "))
for i in range (numero):
    print(mensaje)

nombre = input("ingresa tu nombre y apellido : ")
#opcion 2
print("bienvenido: ", nombre)
#calcular el IMC de esa persona
# leer peso, altura
peso = input("ingresa tu peso en kg : ")
peso = float(peso)
altura  = input (" ingresa tu altura en m : ")
altura = float(altura)
#calculos
IMC = peso/altura**2
#mostrar IMC
print("tu IMC = ", IMC)

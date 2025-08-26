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
# tabla de comparacion 
if IMC >= 18.5 and IMC <= 24.9:
    print ("peso normal")
else:
    if IMC >= 25 and IMC <= 29.9:
        print ("tiene sobre pes0")
    else:
        if IMC >= 30 and IMC <= 34.9:
            print("tiene obesidad I")
        else:
            if IMC > 35 and IMC <= 39.9:
                print("tiene obesidad II")
            else:
                print("tiene obesidad extrema")
                

#otra forma de realizar 

if IMC < 18:
    mensaje = " bajo peso "
elif IMC < 25:
    mensaje = "peso normal"
elif IMC < 35:
    mensaje = "obesidad I"
elif IMC < 40:
    mensaje = "obesidad II"
else:
    mensaje = "obesidad estrema"
print(f"paciente {nombre}, tiene un IMC de {IMC:0.2f} y su condicion es {mensaje}.")

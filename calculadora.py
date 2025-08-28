control = True #variable buleana 

while control == True:
    numero_1 = int(input("escribir un numero: "))
    numero_2 = int(input("ingrese otro numero: "))
    
    print("S. sumar\n R. restar\n M. multiplicar\n D. dividir\n E. salir")
    opcion = input("elija una opcion: ")

    match opcion:
        case 'S':
            print("suma")
            resultado = numero_1 + numero_2
        case 'R':
            print("Resta")
            resultado = numero_1 - numero_2
        case 'M':
            print("multiplicacion")
            resultado = numero_1 * numero_2
        case 'D':
            print("divicion")
            resultado = numero_1 / numero_2 
        case 'E':
            control = False
        
    print(f"resultado = {resultado}")
    

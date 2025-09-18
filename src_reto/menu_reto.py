from modulo_reto.reto import *
def main():
    while True:
        opcion=int(input("1. monitorero temperatura lg: \n 2. monitoreo presion en cabina \n 3. salir"))
        match opcion:
            case 1:
                opcion1 ()
            case 2:
                opcion2()
            case 3:
                break
            case _:
                print ("la opcion no es valida ")


if __name__ == "__main__":
    main()

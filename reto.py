FACTOR_DE_AJUSTE = 0.0004
PRESION_MAXIMA = 11.10
PRESION_MINIMA = 10.9

altitud = float(input("Ingrese la altitud inicial "))
presion_exterior = float(input("Ingrese la presión exterior inicial (en psi): "))

    
presion_cabina_actual = presion_exterior
print(" Simulación iniciada")
print("Presión de cabina inicial igualada a la presión exterior.")

        
while altitud > 0:
    mensaje = ""
            
            
    if altitud <= 10000:
        presion_objetivo = presion_exterior + (altitud * FACTOR_DE_AJUSTE)
        presion_cabina_actual = presion_objetivo
        mensaje = "Ajustando presión de cabina"
    elif 10000 < altitud <= 12000:
        print(" presión estable.")
        presion_objetivo = 11.6 
        presion_cabina_actual = presion_objetivo
        mensaje = "Manteniendo presión de cabina en crucero."
    else:
        presion_objetivo = presion_exterior - (altitud * FACTOR_DE_AJUSTE)
        presion_cabina_actual = presion_objetivo
        mensaje = "Ajustando presión de cabina."

    if presion_cabina_actual > PRESION_MAXIMA:
        presion_cabina_actual -= 0.3
        mensaje = " Exceso de presión"
    elif presion_cabina_actual < PRESION_MINIMA:
        presion_cabina_actual += 0.3
        mensaje = "Baja presión"
    else:
        mensaje = "Presión de cabina óptima."
            
        print(f"Altitud: {altitud}m , Presión Cabina: {presion_cabina_actual} psi")
        print(f"Estado: {mensaje}")

    if altitud == 0:
        if presion_cabina_actual != presion_exterior:
            presion_cabina_actual = presion_exterior
            mensaje = "Avión en tierra"
        else:
            mensaje = "Avión en vuelo"
            
print(f"Aterrizaje completado")
print(f"Estado final: {mensaje}, Presión final: {presion_cabina_actual} psi")

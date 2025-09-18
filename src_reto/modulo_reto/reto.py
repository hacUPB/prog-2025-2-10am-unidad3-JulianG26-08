Factor_de_ajuste = 0.0004
Presion_maxima = 18
Presion_minima = 14

altitud_inicial = float(input("Ingrese la altitud inicial: "))
altitud_crucero = float(input("Ingrese la altitud de crucero : "))
presion_exterior = float(input("Ingrese la presión exterior inicial: "))

presion_cabina_actual = presion_exterior
print("Simulación iniciada")
print("Presión de cabina inicial igualada a la presión exterior.")

altitud = altitud_inicial
subiendo = True

while True:
    if subiendo:
        if altitud < altitud_crucero:
            altitud += 500
            if altitud > altitud_crucero:
                altitud = altitud_crucero
        else:
            subiendo = False
  
    else:
        if altitud > 0:
            altitud -= 500
            if altitud < 0:
                altitud = 0
        else:
            break  

    if altitud <= 10000:
        presion_objetivo = presion_exterior + (altitud * Factor_de_ajuste)
        mensaje = "Ajustando presión de cabina."
    elif 10000 < altitud <= 12000:
        presion_objetivo = 15
        mensaje = "Manteniendo presión de cabina en crucero."
    else:
        presion_objetivo = presion_exterior - (altitud * Factor_de_ajuste)
        mensaje = "Ajustando presión de cabina."

    presion_cabina_actual = presion_objetivo

    if presion_cabina_actual > Presion_maxima:
        presion_cabina_actual -= 0.3
        mensaje += " Exceso de presión"
    elif presion_cabina_actual < Presion_minima:
        presion_cabina_actual += 0.3
        mensaje += " Baja presión"
    else:
        mensaje += "Presión de cabina óptima"

    print(f"Altitud: {altitud:.1f} m , Presión Cabina: {presion_cabina_actual:.2f} psi , Estado: {mensaje}")


if presion_cabina_actual != presion_exterior:
    presion_cabina_actual = presion_exterior
    mensaje = "Avión en tierra"
else:
    mensaje = "Avión en tierra."

print("\nAterrizaje completado")
print(f"Estado final: {mensaje}, Presión final: {presion_cabina_actual:.2f} psi")
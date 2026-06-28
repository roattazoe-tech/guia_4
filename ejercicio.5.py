def calcular_puntos(monto_final_abonado):
    puntos = (monto_final_abonado // 1000) * 5

    if puntos > 50:
        puntos = 50

    return int(puntos)


monto = float(input("Ingrese el monto abonado: "))

print("Puntos ganados:", calcular_puntos(monto))
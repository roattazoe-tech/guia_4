def calcular_recargo(monto_actual, metodo_pago):
    metodo = metodo_pago.lower()

    if metodo == "tarjeta":
        return monto_actual * 1.10
    elif metodo == "efectivo":
        return monto_actual * 0.85
    elif metodo == "transferencia":
        return monto_actual
    else:
        return monto_actual


monto = float(input("Ingrese el monto actual: "))
metodo = input("Ingrese el método de pago: ")

print("Monto final: $", calcular_recargo(monto, metodo))
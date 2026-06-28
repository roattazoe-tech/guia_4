def aplicar_cupon(monto_total, codigo_cupon):
    codigo = codigo_cupon.upper()

    if codigo == "PROA2026":
        return monto_total * 0.85
    elif codigo == "PROAPROA":
        return monto_total * 0.75
    elif codigo == "BELGRANO":
        return monto_total * 0.50
    else:
        return monto_total


monto = float(input("Ingrese el monto total: "))
cupon = input("Ingrese el código de cupón: ")

print("Monto con descuento: $", aplicar_cupon(monto, cupon))
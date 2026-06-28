producto = input("Ingrese el producto (Pendrive, Funda o Cargador): ").lower()
cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
distancia_entrega = float(input("Ingrese la distancia de entrega: "))
cupon_cliente = input("Ingrese el código de cupón: ")
medio_pago = input("Ingrese el método de pago: ")

if producto == "pendrive":
    precio = 7500
    stock = 7
elif producto == "funda":
    precio = 3500
    stock = 5
elif producto == "cargador":
    precio = 9000
    stock = 10
else:
    print("Producto no válido.")
    exit()

if verificar_stock(cantidad_comprada, stock):

    subtotal_productos = precio * cantidad_comprada

    monto_con_descuento = aplicar_cupon(subtotal_productos, cupon_cliente)

    monto_con_recargo = calcular_recargo(monto_con_descuento, medio_pago)

    costo_envio = calcular_envio(distancia_entrega)

    total_final = monto_con_recargo + costo_envio

    puntos = calcular_puntos(total_final)

    mostrar_resumen(subtotal_productos, costo_envio, total_final, puntos)

else:
    print("Compra cancelada: No hay stock suficiente.")

    
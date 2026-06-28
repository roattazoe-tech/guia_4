def mostrar_resumen(monto_productos, costo_envio, monto_final, puntos):
    print("\n--- RESUMEN DE COMPRA ---")
    print("Subtotal Productos: $", monto_productos)
    print("Costo de Envío: $", costo_envio)
    print("Total a Pagar: $", monto_final)
    print("Puntos Ganados:", puntos)
    print("-------------------------")


mostrar_resumen(15000, 2500, 17500, 50)
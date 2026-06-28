def verificar_stock(cantidad_solicitada, stock_disponible=10):
    if cantidad_solicitada <= stock_disponible:
        return True
    else:
        return False


while True:
    cantidad = int(input("Ingrese la cantidad solicitada (-1 para salir): "))

    if cantidad == -1:
        break

    if verificar_stock(cantidad):
        print("Hay stock suficiente.")
    else:
        print("No hay stock suficiente.")
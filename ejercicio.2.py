def calcular_envio(distancia_km):
    if distancia_km <= 5:
        return 2000
    else:
        kilometros_extra = distancia_km - 5
        return 2000 + (kilometros_extra * 500)


distancia = float(input("Ingrese la distancia en km: "))
print("Costo de envío: $", calcular_envio(distancia))
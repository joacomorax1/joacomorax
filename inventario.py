try:
    existencia = int(input("Ingrese la cantidad existente: "))
    vendidos = int(input("Ingrese la cantidad vendida: "))

    if existencia < 0 or vendidos < 0:
        print("Error: los valores no pueden ser negativos.")

    elif vendidos > existencia:
        print("Error: ventas superiores al inventario.")

    else:
        restante = existencia - vendidos
        print("Inventario restante:", restante)

except ValueError:
    print("Error: debe ingresar valores numéricos.")
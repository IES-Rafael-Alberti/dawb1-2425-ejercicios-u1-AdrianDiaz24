# Escribir un programa que pregunte el nombre el un producto, su precio y un 
# número de unidades y muestre por pantalla una cadena con el nombre del producto 
# seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número 
# de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales


def precio_unitario(precio:str) -> str:
    a = precio.find(".")
    centimos = ".00"
    precio_u = "000000.00"
    i = -1
    if a == -1:
        precio = precio+centimos
    b = -1
    precio_u = precio.rjust(9,"0")

    return precio_u


def unidades_t(unidades:str):
    unidades_r = unidades.rjust(3,"0")
    return unidades_r


def coste_t(precio:float, unidades:int):
    coste_total = precio*unidades
    return coste_total


def main ():
    nombre = input("Introduce el nombre del producto: ")
    precio = input("Introduce el precio unitario: ")
    unidades = input("Introduce el nº de unidades disponibles: ")
    precio_u = precio_unitario(precio)
    unidades_r = unidades_t(unidades)
    coste_total = coste_t(float(precio), int(unidades))
    print(f"- {nombre} - {precio_u} - {unidades_r} - {coste_total:011.2f}")
    return 0

if __name__ == "__main__":
    main()
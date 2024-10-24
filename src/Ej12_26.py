# Escribir un programa que pregunte por consola por los productos de una 
# cesta de la compra, separados por comas, y muestre por pantalla cada uno de 
# los productos en una línea distinta.


def pedir_compra():
    compra = str(input("Introduce los poductos de tu cesta de la compra, separa cada producto entre si por una coma: "))
    return compra


def separar_productos(compra:str):
    productos = compra.split(",")
    for producto in productos:
        producto = producto.strip()
        print (f"- {producto}")
    return 0


def main():
    compra = pedir_compra()
    separar_productos(compra)
    return 0

if __name__ == "__main__":
    main()
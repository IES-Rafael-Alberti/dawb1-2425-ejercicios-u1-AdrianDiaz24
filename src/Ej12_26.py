# Escribir un programa que pregunte por consola por los productos de una 
# cesta de la compra, separados por comas, y muestre por pantalla cada uno de 
# los productos en una línea distinta.


def pedir_compra():
    compra = str(input("Introduce los poductos de tu cesta de la compra, separa cada producto entre si por una coma: "))
    return compra


def separar_productos(compra:str):
    a = compra.count(",")
    i =0
    i_2 = 0
    producto = ""
    compra_m = ""
    while i < a:
        b = compra.find(",")
        while i_2 < b:
            producto = producto+compra[i_2]
            i_2 = i_2+1
        print(f"- {producto}")
        c = len(compra)
        i_3 = b
        while i_3 < c:
            compra_m = compra_m+compra[i_3]
            i_3 = i_3+1
        compra  = compra_m        
    i = i+1
    return producto


def main():
    compra = pedir_compra()
    separar_productos(compra)
    return 0

if __name__ == "__main__":
    main()
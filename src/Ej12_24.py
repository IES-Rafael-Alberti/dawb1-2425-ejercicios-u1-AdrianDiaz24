# Escribir un programa que pregunte por consola el precio de un producto en euros 
# con dos decimales y muestre por pantalla el número de euros y el número de 
# céntimos del precio introducido.


def pedir_precio():
    precio = float(input("Dame el percio de producto siguiendo el siguiente formato (x.xx): "))
    precio = round(precio,2)
    precio=str(precio)
    return precio


def separar_precio_e(precio:str):
    a =  precio.find(".")
    i = 0
    x = 0
    euros = ""
    while i < a:
        euros=euros+precio[x]
        x= x+1
        i = i+1
    return euros


def separar_precio_c(precio:str):
    a = precio.find(".")+1
    i = len(precio)
    centimos = ""
    while a <= i:
        centimos = centimos+precio[a]
        a = a+1
        return centimos


def main():
    precio = pedir_precio()
    euros = separar_precio_e(precio)
    centimos = separar_precio_c(precio)
    print(euros)
    print(centimos)
    return 0

if __name__ == "__main__":
    main()
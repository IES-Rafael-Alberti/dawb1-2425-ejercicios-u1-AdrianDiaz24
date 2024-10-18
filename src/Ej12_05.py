#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA ~
#a aplicar y calcule e imprima por pantalla el precio final del artículo.

def pedir_precio():
    precio = float(input("Dame el precio sin IVA del producto: "))
    return precio


def pedir_iva():
    iva = float(input("Dame el IVA a aplicar: "))
    return iva

def calcular_precio(a, b):
    precio_final = a*(1+(b/100))
    return precio_final


def main():
    precio = pedir_precio()
    iva = pedir_iva()
    precio_final = calcular_precio(precio, iva)

    print(f"El precio final del producto es ", round(precio_final,2))
    return 0

if __name__ == "__main__":
    main()
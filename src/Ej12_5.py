#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA ~
#a aplicar y calcule e imprima por pantalla el precio final del artículo.

def pedir_precio():
    precio = float(input("Dame el precio sin IVA del producto: "))
    return precio


def pedir_iva():
    iva = float(input("Dame el IVA a aplicar: "))
    return iva
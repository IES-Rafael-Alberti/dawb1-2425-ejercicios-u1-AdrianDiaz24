#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA 
#que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

def importe_final():
    importe_f = float(input("Dime el importe final del producto: "))
    return importe_f


def iva_pagado(importe_f):
    iva_p = 10/100 * importe_f
    return iva_p


def importe_sin_iva(importe_f, iva_p):
    importe_p = importe_f - iva_p
    return importe_p


def main():
    
    return 0

if __name__ == "__main__":
    main()
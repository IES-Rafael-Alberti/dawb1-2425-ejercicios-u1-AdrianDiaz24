# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del 
# país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un 
# número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


def pedir_tlf():
    tlf = str(input("Introduce el nº de tlf que deseas llamar siguiendo el siguiente formato (prefijo-tlf-extension): "))
    return tlf


def conseguir_tlf_s(tlf:str):
    x = tlf.index("-")+1
    i = 0
    tlf_s = str()
    while i < 9:
        tlf_s = tlf_s + tlf[x]
        x = x+1
        i = i+1
    return tlf_s


def main():
    tlf = pedir_tlf()
    tlf_s = conseguir_tlf_s(tlf)

    print(tlf_s)

    return 0

if __name__ == "__main__":
    main()
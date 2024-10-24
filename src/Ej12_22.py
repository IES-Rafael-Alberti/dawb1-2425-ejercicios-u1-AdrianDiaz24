# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre 
# por pantalla la misma frase pero con la vocal introducida en mayúscula.


def pedir_frase():
    frase = str(input("Introduce una frase: "))
    return frase


def pedir_vocal():
    vocal = str(input("Introduce una vocal que volver mayusculas: "))
    return vocal


def convertir_frase(frase:str, vocal:str):
    x = len(frase)
    frase_c = str("")
    i = 0
    while i < x:
        y = frase[i]
        if y == vocal:
            frase_c = str(frase_c + frase[i].upper())
            i = i+1
        else:
            frase_c = str(frase_c + frase[i])
            i = i+1
    return frase_c
    


def main():
    frase = pedir_frase()
    vocal = pedir_vocal()
    frase_c = convertir_frase(frase, vocal)
    print(frase_c)
    return 0

if __name__ == "__main__":
    main()
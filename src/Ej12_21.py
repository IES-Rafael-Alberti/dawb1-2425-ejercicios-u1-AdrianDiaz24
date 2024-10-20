#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


def pedir_frase():
    frase = str(input("Dime una frase que invertir: "))
    return frase


def invertir_frase(frase:str):
    x = len(frase)
    y = -1
    frase_i = ""
    while y > -x:
        frase_i = frase_i + frase[::y]
        y = y-1
        return frase_i


def main():
    frase = pedir_frase()
    frase_i = invertir_frase(frase)
    print(f"La frase invertida es: {frase_i}")
    return 0

if __name__ == "__main__":
    main()
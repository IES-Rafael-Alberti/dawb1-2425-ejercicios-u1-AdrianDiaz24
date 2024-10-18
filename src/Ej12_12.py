#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#  calcule el índice de masa corporal y lo almacene en una variable,
#  y muestre por pantalla la frase Tu índice de masa corporal es donde es el
#  índice de masa corporal calculado redondeado con dos decimales.

def pedir_peso():
    peso = float(input("Dame tu peso en Kg: "))
    return peso


def pedir_altura():
    altura = float(input("Dame tu altura en metros: "))
    return altura


def calcular_imc(h,m):
    imc = (m/(h**2))
    return imc


def main():
    h = pedir_altura()
    m = pedir_peso()
    imc = calcular_imc(h, m)
    print(f"Tu índice de masa corporal es {imc} donde {round(imc,2)} es el  índice de masa corporal redondeado a dos decimales.")
    return 0

if __name__ == "__main__":
    main()
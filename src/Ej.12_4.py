#Escribe un programa que le pida al usuario 
# una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima 
# por pantalla la temperatura convertida.

def pedir_celcius():
    celsius = float(input("Dame una temperatura en Celsius: "))
    return celsius


def convertir_fahrenheit(celsius):
    fahrenheit = (9/5)*celsius+32
    return fahrenheit


def main():

    return 0
if __name__ == "__main__":
    main()
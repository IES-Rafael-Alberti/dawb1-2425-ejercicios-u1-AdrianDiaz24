# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de 
# interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales 
# de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la
# cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y 
# mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.


def pedir_dinero():
    dinero = float(input("Dime cuanto dinero has añadido: "))
    return dinero



def calcular_beneficio(dinero):
    i = 1
    while i <= 3:
        beneficio = (dinero*1.04)*i
        print(f"El dinero generado el {i}º año es de {round(beneficio, 2)}")
        i = i+1
    return 0


def main():
    dinero = pedir_dinero()
    calcular_beneficio(dinero)

    return 

if __name__ == "__main__":
    main()


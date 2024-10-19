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
    beneficio = dinero
    print(f"Has ingresado {round(dinero,2)}€")
    while i <= 3:
        beneficio = (beneficio*1.04)
        dinero_g = (beneficio-dinero)
        print(f"El importe total de su cuenta despues del {i}º año es de {round(beneficio, 2)}€, habiendo generado {round(dinero_g,2)}€")
        i = i+1
    return print ("Recuerde que este benecio se vera alterado si retira o ingresa mas dinero.")


def main():
    dinero = pedir_dinero()
    calcular_beneficio(dinero)

    return 

if __name__ == "__main__":
    main()


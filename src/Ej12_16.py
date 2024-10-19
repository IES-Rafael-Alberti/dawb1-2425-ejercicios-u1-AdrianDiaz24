# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe 
# mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se 
# le hace por no ser fresca y el coste final total de todas las barras no frescas.


def barras_vendidas():
    barras = int(input("Dime las barras de pan no frescas vendidas: "))
    return barras


def aplicar_descuento(barras, precio):
    precio_f = (precio*0.40)*barras
    return precio_f


def main():
    precio = 3.49
    barras = barras_vendidas()
    precio_f = aplicar_descuento(barras, precio)

    print(f"- Precio habitual por barra: {precio}€ \n- Descuento por no ser fresca: 60% \n- Precio final de {barras} barra/s vendidas {round(precio_f,2)}€",  )

    return 0

if __name__ == "__main__":
    main()

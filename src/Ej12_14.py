# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de 
# cada paquete así que deben calcular el peso de los payasos y muñecas que 
# saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el 
# último pedido y calcule el peso total del paquete que será enviado.

def pedir_muñecas():
    muñecas = int(input("Dime cuantas muñecas vas a enviar: "))
    return muñecas


def pedir_payaso():
    payasos = int(input("Dime cuantos payasos vas a enviar: "))
    return payasos


def calcular_peso(payasos,muñecas):
    peso_t = (payasos*112)+(muñecas*75)
    return peso_t


def convertir_kg(peso_t):
    peso_t_kg = float(peso_t/1000)
    peso_t_kg = round(peso_t_kg,2)
    return peso_t_kg


def main():
    payasos = pedir_payaso()
    muñecas = pedir_muñecas()
    peso_t = calcular_peso(payasos, muñecas)

    if peso_t <= 1000:
        print(f"El peso del envio de {muñecas} muñeca/s y {payasos} payaso/s es de {peso_t}g")
        return 0
    else:
        peso_t_kg = convertir_kg(peso_t)
        print(f"El peso del envio de {muñecas} muñeca/s y {payasos} payaso/s es de {peso_t_kg}Kg")
        return 0

if __name__ == "__main__":
    main()
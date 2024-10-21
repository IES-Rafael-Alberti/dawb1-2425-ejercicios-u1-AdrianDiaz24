# Escribir un programa que pregunte al usuario la fecha de su nacimiento en 
# formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el 
# mes se introduzcan con un solo carácter.


def pedir_fecha():
    año = str(input("Introducaz su fecha de nacimiento, (siguiento este formato: dd/mm/aaaa): "))
    return año
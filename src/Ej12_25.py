# Escribir un programa que pregunte al usuario la fecha de su nacimiento en 
# formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el 
# mes se introduzcan con un solo carácter.


def pedir_fecha():
    fecha = str(input("Introducaz su fecha de nacimiento, (siguiento este formato: dd/mm/aaaa): "))
    return fecha


def conseguir_año(fecha_sin_d:str):
    a = fecha_sin_d.find("/")+1
    b= len(fecha_sin_d)
    año  = ""
    while a < b:
        año = año+fecha_sin_d[a]
        a = a+1
    return año

def quitar_dia(fecha:str):
    a = fecha.find("/")+1
    b = len(fecha)
    fecha_sin_d = ""
    while a < b:
        fecha_sin_d = fecha_sin_d+fecha[a]
        a = a+1 
    return fecha_sin_d


def conseguir_mes(fecha_sin_d:str):
    a = fecha_sin_d.find("/")
    i = 0
    mes = ""
    while i < a:
        mes = mes+fecha_sin_d[i]
        i = i+1
    return mes


def conseguir_dia(fecha:str):
    a = fecha.find("/")
    i = 0
    dia = ""
    while i < a:
        dia = dia+fecha[i]
        i = i+1
    return dia


def main():
    fecha = pedir_fecha()
    dia = conseguir_dia(fecha)
    fecha_sin_d = quitar_dia(fecha)
    mes = conseguir_mes(fecha_sin_d)
    año = conseguir_año (fecha_sin_d)
    print(f"- Naciste el {dia} del {mes} de {año}")
    return 0

if __name__ == "__main__":
    main()
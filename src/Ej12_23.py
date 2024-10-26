# Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @)
# pero con dominio ceu.es.


def pedir_correo():
    correo = str(input("Introduce tu correo electronico: "))
    return correo


def convertir_correo(correo:str):
    a = correo.find("@")
    correo_c = ""
    i = 0
    while i < a:
        correo_c = correo_c+correo[i]
        i = i+1
    return correo_c


def main():
    correo = pedir_correo()
    correo_c = convertir_correo(correo)
    print(f"- Tu nuevo correo es: {correo_c}@ceu.es" )
    return 0

if __name__ == "__main__":
    main()
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre 
# combinando mayúsculas y minúsculas como quiera.


def pedir_nombre():
    nombre = str(input("Dame tu nombre completo: "))
    return nombre


def convertir_min(nombre:str):
    minuscula = nombre.lower()
    return minuscula


def convertir_mayus(nombre:str):
    mayusculas = nombre.upper()
    return mayusculas


def convertir_iniciales(nombre:str):
    iniciales = nombre.title()
    return iniciales


def main():
    nombre = pedir_nombre()
    print(f"- {convertir_min(nombre)}")
    print(f"- {convertir_mayus(nombre)}")
    print(f"- {convertir_iniciales(nombre)}")
    return 0

if __name__ == "__main__":
    main()
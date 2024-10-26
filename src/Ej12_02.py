
def pedir_horas():
    horas = float(input("Dime las horas trabajadas: "))
    return horas

def pedir_precio():
    precio =  float(input("Dime el precio por hora: "))
    return precio

def calcular_importe(horas, precio):
    return horas * precio

def main():
    horas = pedir_horas()
    precio = pedir_precio()
    importe = calcular_importe(horas,precio)
    print("Importe toral: ", importe)
    return 0

if __name__ =="__main__":
    main()




repetir=int(input("Ingrese un 2 para comenzar, un 1 para terminar el programa : "))
while repetir!=1:
    try:

        num1=int(input("Ingrese un numero: "))
        num2=int(input("ingrese otro numero: "))
        suma=num1+num2
        print("la suma de los 2 es: ",suma)
        repetir=int(input("si quiere continuar sumando ingrese un 2,ingrese un 1 si quiere terminar el programa: "))
    except ValueError as e:
        print("ingrese un numero valido")
        pass

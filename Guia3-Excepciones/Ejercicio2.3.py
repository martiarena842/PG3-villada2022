

try:
    num1=int(input("ingrese un numero: "))
    num2=int(input("ingrese un numero: "))
    div=num1/num2

    print("La division da= ",div)

except ZeroDivisionError:
    print("no se puede dividir por cero, ingrese un numero valido. ")
    pass
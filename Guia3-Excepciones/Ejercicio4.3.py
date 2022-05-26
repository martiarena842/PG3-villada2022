try:
    num1=int(input("Introduce un numero: "))
    num2=int(input("Introduce otro numero: "))
    div=num1/num2
    print("La division es: ",div)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
    pass
except ValueError:
    print("ingrese un numero validoo")
    pass


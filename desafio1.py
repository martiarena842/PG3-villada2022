# def triangulo(A,ancho):

# for i in range(ancho):
#  print(ancho*A)


from ntpath import join


ancho = int(input("ingresa el alto: "))
A = str(input("Ingresa caracter: "))
prim = ancho + 1
first = " " * prim
contador = 0


print("" + first + A)
if ancho > 1:
    contador = 1
    while contador < ancho:
        k = ancho - contador
        print(" " * k, contador * A + " ".join(A) + contador * A)
        contador = contador + 1
else:

    while contador != abs(ancho):

        k = ancho + contador
        print(" " * k, contador * A + " ".join(A) + contador * A)
        contador = contador + 1


# " "+A*contador
# contador=alto +1

from ntpath import join


ancho = int(input("ingresa el alto: "))
A = str(input("Ingresa caracter: "))
prim = ancho + 1
first = " " * prim
juan = 0


if ancho > 1:
    print("" + first + A)
    contador = 1
    while contador < ancho:
        k = ancho - contador
        print(" " * k, contador * A + " ".join(A) + contador * A)
        contador = contador + 1
else:
    contador = 0
    contador = abs(ancho)
    while juan < 10:

        contador = contador - 1
        k = contador - 1
        print(+contador * A + " " * k)

        juan = juan + 1
print("probando")
# " "+A*contador
# contador=alto +1

# k = ancho + contador
# print(" " * k, contador * A + " ".join(A) + contador * A)
# contador = contador + 1

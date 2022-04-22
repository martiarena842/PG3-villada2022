def anobisiesto(ano):

    if (ano % 400 == 0) or (ano % 100 != 0) and (ano % 4 == 0):
        print("es un anio bisiesto")

    else:
        print("No es un anio bisiesto")


ano = int(input("INgresa un anio: "))

anobisiesto(ano)

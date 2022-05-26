try:
    f = open("Guia3-Excepciones/manejodeexcepciones.txt", "a")
    f.write(" Now the file has more content!")
    contenido=input("ingrese lo que quiere poner en el texto")
    
    caracteres = set("0123456789")

    if all((c in caracteres) for c in contenido):
        f.write(int(contenido))
    else:
        f.write(contenido)

    f = open("Guia3-Excepciones/manejodeexcepciones.txt", "r")
    print(f.read())
    f.close()

except TypeError:
    print("no se pueden ingresar enteros en el metodo write")
    pass

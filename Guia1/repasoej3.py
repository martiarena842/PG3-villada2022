def rectangulo(alto, ancho, A):
    for x in range(alto):
        print(ancho * A)


ancho = int(input("ingresa el ancho: "))
A = str(input("Ingresa caracter: "))
alto = int(input("Ingresa la altura: "))

# Todo@martiarena842
rectangulo(ancho, A, alto)

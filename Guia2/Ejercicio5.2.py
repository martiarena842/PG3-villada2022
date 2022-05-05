class persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)

persona1=persona()
persona1.imprimir()

class empleado(persona):

    def __init__(self):
        self.salario=int(input("Ingrese su salario: "))

    def imprimir(self):
        print("su salario es de: ",self.salario)

    def impuesto(self):
        if self.salario>=3000:
            print("tiene que pagar impuestos")
        else:
            print("no tiene que pagar impuestos")


empleado1=empleado()
empleado1.imprimir()
empleado1.impuesto()

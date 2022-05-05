class Familia:

    def __init__(self):
        self.nombrep = input("ingrese el nombre del padre: ")
        self.nombrem=input("ingrese el nombre de la madre: ")
        self.nombreh =list=[]
        self.numhijos=int(input("ingrese el numero de hijardos "))

        for i in range(self.numhijos):
            self.nombres=str(input("ingrese el nombre de les hijes "))
            self.nombreh.append(self.nombres)

    def __str__(self):
        return "el nombre del padre es: {}\nel nombre de la madre es: {}\nel numero de hijos es: {}\nel nombre de los hijos es: {}".format(self.nombrep,self.nombrem,self.numhijos,self.nombreh)
    

f1=Familia()
print(f1)

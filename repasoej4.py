from ast import Num


lista = []
 
def sorta(num):
    
    num = int(input("Ingrese el numero de elementos de la lista: "))
    

    for i in range(0, num):
        ele = int(input())
 
        lista.append(ele) 
    lista.sort(reverse=True)
    print(lista)

sorta(lista)
 


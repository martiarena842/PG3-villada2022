print ("Ingrese el numero q quiere b")
mi_lista = [ 2,6,8,20,1,3,99 ]
num= int(input("")) 
#xa=mi_lista.index(num)
#print(" el numero esta en: ",xa)

def lista (mi_lista, num):
    for xa in mi_lista:
        if xa==num:
            numerardo=mi_lista.index(num)
            print("el numero esta en: "+str(numerardo))

lista(mi_lista, num)

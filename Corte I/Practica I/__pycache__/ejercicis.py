#declarar una lista vacia 
lista=[]
#pedir al usuario que ingrese la cantidad de superheroes que quiere añadir 
numero=int(input("digite la cantidad de superheroes que quiere añadir "))
#hacer un for para iterar la lista completa 
for i in range(numero):
    superheroe=input ("Digite nombre del superheroe :")
    #Funcion para ir agregando superheroes metodo append
    lista.append(superheroe)

    #imprimimos la lista 
    print(lista)

#VOY A CREAR UNA LISTA Y LA VOY A ORGANIZAR  DE FORMA ASCENTENDE Y DESCENTENTE CON EL METODO BURBUJA 

lista=[1,5,7,9,3,2,4,6,8]
#len funciona para mirar toda la lista 
n=len(lista)
#crear un for para iterar la lista 
for i in range(n):
#crear un for j para iterar la siguiente posicion 
    for j in range (0,n-i-1):
#el condicional que me va a mostrar si la lista la quiere de forma ascentende o descendente 
        if lista [j]>lista[j+1]:
        #esto me va a ir comprarando de posicion en posicion 
            lista[j],lista[j+1]=lista[j+1],lista[j]

#imprimir la lista 
print(lista)




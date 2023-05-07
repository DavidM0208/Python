lista=[1,2,3,4]
#Mostrar contenido de una lista
#print(lista)
#Acceder a un elemento  de  una lista
#print(lista[0])
#Ultimo elemento de una lista
#print(lista[-1])
#Modifiiccar elemento de una lista 
lista[0]=7
print(lista)
#Iterar reciorrer una lista
#for l in lista:
#    print(l)
#Si necesitamos un index que acompañe cada dato
for index, l in enumerate(lista):
    print(index, l)
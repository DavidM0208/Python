#Declaración de un metodo.
def sumar():
    print("Este es el metodo sumar.")

#Declaración de metodo con parametros.
def restar(n1, n2):
    #Cuerpo del metodo.
    restar = n1 - n2
    print(f"La resta entre {n1} y {n2} es {restar}.")

#Declaración de metodo con valor de retorno.
def multiplicar(n1, n2):
    #Cuerpo del metodo.
    multiplicar = n1 * n2
    #Retorno del dato.
    return multiplicar


#Llamado o invocación del metodo.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

print("Menu de opciones:")
op = input("Ingrese la oopción segun la operación a realizar: \n1. Suma. \n2. Restar. \n3. Multipicación. \n4. División.\n")

if op == "1":
    #Definición o invocaión del metodo sumar.
    sumar()

elif op == "2":
    #Definición o invocaión del metodo con parametros.
    restar(n1,n2)
    

elif op == "3":
    #Definición o invocaión del metodo con valor de retorno.
    #multiplicar(n1,n2)
    #Forma de usar el metodo con valor de retorno directamente en una impreción.
    print(f"La multiplicación entre {n1} y {n2} es {multiplicar(n1,n2)}.")

    #Guardar en una variable para operarlo en otro momento.
    producto = multiplicar(n1,n2)
    if producto < 50:
        print("El producto es menor que 50.")
    else:
        print("El producto es mayor que 50.")

presuspuesto = 100000
op = 1
opcion1 = 0
opcion2 = 0
opcion3 = 0
#Acumulador.

#Opcion 1 = Pagar transporte, descuenta  6000.
#Opcion 2 = Gastar onces a la profe, descuenta 10000.
#Opcion 3 = Ganar dinero, aunmenta 5000.

#Que se repita las veces que el usuario desee.
#Poner el conteo de las veces que se escogio cada opción y cuando desconto o aumento en cada una de ellas.

print("Opción 1: Pagar transporte.")
print("Opción 2: Gastar onces a la profesora.")
print("Opción 3: Gabar dinero.")

while op==1:

    msg = int(input("Digite un número entre 1 y 3 para escoger la opción que desea hacer: "))

    if msg == 1:
        resultado = presuspuesto - 6000
        opcion1 = opcion1 + 1
        print(f"Usted pago el transporte, su presupuesto ahora es {resultado}")
    elif msg == 2:
        resultado = presuspuesto - 10000
        opcion2 = opcion2 + 1
        print(f"Usted le gasto onces a la profe, su presupuesto ahora es {resultado}")
    elif msg == 3:
        opcion3 = opcion3 + 1
        resultado = presuspuesto + 5000
        print(f"Usted gano dinero, su presupuesto ahora es {resultado}")
    else:
        print("Opción incorrecta.")

    presuspuesto = resultado

    op=int(input("Digite 1 si desea escoger otra opción, de lo contrario digite 2 "))

print(f"La  cantidad de veces que se repitio cada opción con la suma de lo que se gasto es: \n Opción 1: {opcion1}, {opcion1*6000} \n Opción 2: {opcion2}, {opcion2*10000} \n Opción 3: {opcion3}, {opcion3*5000}")

presuspuesto = 100000

#Acumulador.

#Opcion 1 = Pagar transporte, descuenta  6000.
#Opcion 2 = Gastar onces a la profe, descuenta 10000.
#Opcion 3 = Ganar dinero, aunmenta 5000.

#Esto se puede ejecutar 5 veces y el usuario puede  escoger cualquiera de las opciones de arriba.

print("Opción 1: Pagar transporte.")
print("Opción 2: Gastar onces a la profesora.")
print("Opción 3: Gabar dinero.")

for i in range (1,6):

    msg = int(input("Digite un número entre 1 y 3 para escoger la opción que desea hacer: "))

    if msg == 1:
        resultado = presuspuesto - 6000
        print(f"Usted pago el transporte, su presupuesto ahora es {resultado}")
    elif msg == 2:
        resultado = presuspuesto - 10000
        print(f"Usted le gasto onces a la profe, su presupuesto ahora es {resultado}")
    elif msg == 3:
        resultado = presuspuesto + 5000
        print(f"Usted gano dinero, su presupuesto ahora es {resultado}")
    else:
        print("Opción incorrecta.")

    presuspuesto = resultado

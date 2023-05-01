celular = 3209161848
contra = 1234
saldo = 4500
op = "s" or "S"
intentos = 3

for i in range (1,4):

    msg = int(input("Ingrese el número de celular: \n "))
    password=int(input("Digite los 4 digitos de su contraseña: \n"))

    if msg == celular and password == contra:

        while op == "s" or "S":
            print(f"¡Bienvenido a nequi! \n Su saldo es de: {saldo}")
            select = int(input("Digite 1 para sacar dinero. \nDigite 2 para enviar dinero. \nDigite 3 para recargar dinero. \nDigite 4 para salir. \n"))

            if select == 1:
                opcion = int(input("Digite 1 para sacar el dinero por cajero. \nDigite 2 para punto fisico.\n"))
                if opcion == 1:
                    print(f"Su saldo actual es: {saldo}")
                    retiro = int(input("¿Cuanto desea retirar?\n"))
                    if retiro > saldo:
                        print("No tienes fondos para retirar.")
                    elif retiro <= saldo:
                        saldo = saldo - retiro
                        print("Su codigo es: 987654")
                        print(f"Su saldo actual es {saldo}")
                    elif retiro < 2000:
                        print("No te alcanza.")
                elif opcion == 2:
                    print(f"Su saldo actual es: {saldo}")
                    retiro = int(input("¿Cuanto desea retirar?\n"))
                    if retiro > saldo:
                        print("No tienes fondos para retirar.")
                    elif retiro <= saldo:
                        saldo = saldo - retiro
                        print("Su codigo es: 987654")
                        print(f"Su saldo actual es {saldo}")
                    elif retiro < 2000:
                        print("No te alcanza.")

            elif select == 2:
                print(f"Su saldo actual es {saldo}")
                numero = int(input("Ingrese el número de telefono al que desea enviar el dinero.\n"))
                valor = int(input("Ingrese el valor que desea enviar.\n"))
                if valor > saldo:
                    print("No tienes fondos suficientes para enviar.")
                elif valor <= saldo:
                    saldo = saldo - valor 
                    print(f"Usted ha enviado {valor} al número {numero}, le quedo  un saldo de {saldo}")

            elif select == 3:
                recarga = int(input("Ingrese el valor que desea recargar.\n"))
                preg = int(input("Digite 1 para realizar la recarga. De lo contrario digite 2\n"))
                if preg == 1:
                    saldo = saldo + recarga
                    print(f"Su recarga ha sido realizada exitosamente, su saldo actual es {saldo}")
                elif preg == 2: 
                    print("Ha cancelado la recarga.")
            elif select == 4:
                print("Gracias por usar nequi.")
        op = input("Si desea elegir otra opcion, escriba SI. De lo contrario escriba NO.\n")

        saldo = saldo -retiro

    else:
        intentos = intentos - 1
        print(f"¡Upps! Parece que tus datos de acceso no son correctos, Tienes {intentos} intentos más")
        
        if intentos == 0:
            print("Ha agotado todos sus intentos.")
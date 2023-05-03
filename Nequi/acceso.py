saldo = 4500
op = 1
intentos = 3

for i in range (1,4):

    celular = int(input("Ingrese el número de celular: \n "))
    password=int(input("Digite los 4 digitos de su contraseña: \n"))

    if celular == 3209161848 and password == 1234:

        while op == 1:
            print(f"¡Bienvenido a nequi! \n Su saldo es de: {saldo}")
            select = int(input("Digite 1 para sacar dinero. \nDigite 2 para enviar dinero. \nDigite 3 para recargar dinero. \nDigite 4 para ahorrar dinero.\nDigite 5 para hacer una recarga a celular. \nDigite 6 para salir. \n"))

            if select == 1:
                opcion = int(input("Digite 1 para sacar el dinero por cajero. \nDigite 2 para punto fisico.\n"))
                if opcion == 1 or opcion == 2:
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
                preg = int(input("Digite 1 para realizar la recarga. \nDe lo contrario digite 2.\n"))
                if preg == 1:
                    saldo = saldo + recarga
                    print(f"Su recarga ha sido realizada exitosamente, su saldo actual es {saldo}")
                elif preg == 2: 
                    print("Ha cancelado la recarga.")

            elif select == 4:

                print(f"Su saldo actual es {saldo}")
                ahorro = int(input("¿Cuanto dinero desea ahorrar?\n"))
                saldo = saldo - ahorro
                print(f"Usted ahorro {ahorro}, su nuevo saldo es de {saldo}.")

            elif select == 5:

                print(f"Su saldo actual es {saldo}")
                numero = int(input("Digite el número de celular al que desea recargar.\n"))
                if numero == celular:
                    print(f"Su saldo actual es {saldo}")
                    precio = int("Ingrese el valor de la recagra: \n")
                    saldo = saldo - precio
                    print(f"Su recagra se a realizado con exito al número {numero} de un valor de {precio}")

            elif select == 6:
                print("Gracias por usar nequi.")
                break
                
        op = input("Si desea selecionar otra opción digite 1. De lo contrario digite 2.\n")

        saldo = saldo - retiro

    else:
        intentos = intentos - 1
        print(f"¡Upps! Parece que tus datos de acceso no son correctos, Tienes {intentos} intentos más")
        
        if intentos == 0:
            print("Ha agotado todos sus intentos.")
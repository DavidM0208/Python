fruver = {}

while True:
    print("Bienvenido a Fruver Noé")
    print("1. Añadir/Modificar.")
    print("2. Buscar.")
    print("3. Borrar.")
    print("4. Listar.")
    print("5. Salir.")
    opcion = int(input("Elija una opcion: "))   
    if opcion == 1:
        articulo = input("Ingrese el nombre del artículo: \n")
        if articulo in fruver:
            print("el artículo ya se encuentra registrado.")
            opcion1 = int(input("Digite 1 si desea modificar el precio del artículo. \nDigite 2 si desea modificar el tipo del artículo. \n"))
            if opcion1 == 1:
                precio = int(input("Ingrese el nuevo precio del artículo. \n"))
                fruver [articulo]['Precio'] = precio
            elif opcion1 == 2:
                tipo = int(input("Selecione de que tipo es el artículo. \n1. Vegetal. \n2. Fruta. \n"))
                if tipo == 1:
                    variedad = "Vegetal"
                elif tipo == 2:
                    variedad = "Fruta"
                fruver[articulo]['Tipo'] = variedad
            else:
                print("¡¡ERROR!! Opción no valida.")
            
        else:
            print("El articulo no existe.")
            fruver[articulo] = {}
            precio = int(input("Ingrese el precio del artículo. \n"))
            fruver[articulo]['Precio'] = precio
            tipo = int(input("Selecione de que tipo es el artículo. \n1. Vegetal. \n2. Fruta. \n"))
            if tipo == 1:
                    variedad = "Vegetal"
            elif tipo == 2:
                    variedad = "Fruta"
            fruver[articulo]['Tipo'] = variedad

    elif opcion == 2:
        buscar = input("Ingrese el nombre del articulo que desea buscar: ")
        print("Se encontraron los siguientes resultados:")
        for (articulo,datos) in fruver.items():
            if articulo.startswith(buscar):
                print(articulo)
                print(f"El precio del artículo ingresada es {fruver[articulo]['Precio']} y es de tipo {fruver[articulo]['Tipo']}")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del artículo que desea borrar: ")
        if nombre in fruver:
            borrar = int(input("Digite 1 si desea borrar el artículo del fruver. \nDigite 2 para cancelar la acción. \n"))
            if borrar == 1:
                del fruver[nombre]
                print(f"El artículo {nombre} ha sido eliminado.")
                print(fruver)
            elif borrar == 2:
                print("Usted ha cancelado el proceso de eliminación.")
                print(fruver)
            else:
                print("El artículo {borrar} no existe en el fruver.")
            

    elif opcion == 4:
        for x in fruver:
            print(f"En este fruver usted encuentra {x} con un precio de {fruver[x]['Precio']} y de un tipo {fruver[x]['Tipo']}")


    elif opcion == 5:
         print("Adios")
         break
from random import randint
saldo = 5000
op = 1
def lanzarMoneda():
    nombre = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre} al juego cara y sellazo.")

    moneda = randint(1,2)
    return moneda
def ganar(saldo, apuesta):
    print("Usted ganó.")
    resultado = saldo + apuesta * 2
    print(f"Su nuevo saldo es de {resultado}")

def perder(saldo, apuesta):
    print("Usted perdió.")
    resultado = saldo - apuesta
    print(f"Su nuevo saldo es de {resultado}")

def jugar():
    moneda = lanzarMoneda()
    eleccion = int(input("Digite 1 para escoger cara o 2 para escoger sello.\n"))
    
    if eleccion == 1:
        print("Usted elegio cara.")
    elif eleccion == 2:
        print("Usted elegio sello.")
    apuesta = int(input("¿Cuanto desea apostar?\n"))
    if moneda==1 and eleccion==1:
        ganar(saldo, apuesta)
        print("Salio cara, usted escogio cara, Ganaste!...")
    elif moneda==1 and eleccion==2:
        perder(saldo, apuesta)
        print("Salio cara, usted escogio sello, Perdiste!...")
    elif moneda==2 and eleccion==2:
        ganar(saldo, apuesta)
        print("Salio sello, usted escogio sello, Ganaste!...")
    elif moneda==2 and eleccion==1:
        perder(saldo, apuesta)
        print("Salio sello, usted escogio cara, Perdiste!...")
while op == 1:
    jugar()
    op = int(input("Digite 1 si quiere jugar de nuevo.\nDigite 2 si quiere salir.\n"))
    if op == 2:
        print("Gracias por jugar")
num=int(input("Ingrese un número entre el 1 y el 10: "))

if num < 1 or num > 10:
    print("¡¡ERROR!! Solo es permitido un número entre el 1 y el 10.")
else:
    print(f"La tabla de multiplicar inversa del número {num} es: ")

    for i in range(10, 0, -1):
        print(f'{num} x {i} = {num * i}')
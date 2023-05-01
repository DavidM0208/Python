num=int(input("Ingrese un número entre el 1 y el 10: "))

if num < 1 or num > 10:
    print("¡¡ERROR!! Solo es permitido un número entre el 1 y el 10.")
else:
    print(f"La tabla de multiplicar del número {num} es: ")

    for i in range(1, 11):
      resultado = num * i
      print(f'{num} x {i} = {resultado}')
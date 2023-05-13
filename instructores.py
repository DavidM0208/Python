# Se crean 2  diccionarios con key y values
i1 = {
    "Nombres": "Jennifer Andrea",
    "Apellidos": "Fajardo Bolívar",
    "Title": "Ingeniera de Sistemas"
}
i2 = {
    "Nombres": "Jonathan",
    "Apellidos": "Espitia",
    "Title": "Tecnologo en Sistemas"
}
# Diccionario anidado. Se crea un diccionario madre para llamar los diccionarios hijos. Sobre este dicionario anidado funcionan los mismo elementos
instructores = {
    "instructores1": i1,
    "instructores2": i2
}
print(instructores)
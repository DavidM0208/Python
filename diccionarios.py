# Definir un diccionario
# Las variables de la izquierda son llamadas keys y las de la derecha son values (Valores) 
persona={
    "first_name": "Sergio David",
    "last_name": "Cifuentes Ramos",
    "age": 23,
    "id": 123456789,
    "state": True 
}
# Diccionario vacio
# persona={}
# Imprimimos el diccionario para ver los datos del mismo
print(persona)
# Para mostrar un valor en particular del diccionario
# print(persona['first_name'])
# Tambien para mostrar un valor en particular se puede usar el método get
# print(persona.get('last_name'))
# Se puede modificar los elementos del diccionario a través de su key (Se le llama propiedad mutable en los diccionarios)
persona['first_name'] = "Juan Camilo"
print(persona)
# Si accedemos a un key que no existe este se añadira automaticamente al diccionario
persona['title'] = "Ingeniero de sistemas"
print(persona)
# Tambien se puede usar el método update, que accede al diccionario, y a través del key modifica su valor
persona.update({"last_name": "Susa Gomez"}) 
print(persona)
# Borrar un elemento del diccionario basandose en la key indicada 
persona.pop("title")
print(persona)
# Borrar el ultimo elemento del diccionario 
persona.popitem()
print(persona)
# Borrar del diccionario una key  especifica
del persona["id"]
print(persona)
# Borrar el diccionario completo 
# del persona
# persona.clear()
# Muestra los key del diccionaro
for i in persona:
    print(i)
# Muestra los values del diccionario
for z in persona:
    print(persona[z])
# Muestra cada par de key y values del diccionario
for x, y in persona.items():
    print(x,":", y)


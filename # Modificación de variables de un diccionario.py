# Modificación de variables de un diccionario.

# Creamos diccionario vacío.
heroe = {}

# ¿Cuántos héroes quiere añadir?
cantidad = int(input("¿Cuántos personajes quieres añadir? "))

# Iteramos para añadir al diccionario.
for i in range(cantidad):
    pj_Name = input(f"\nNombre del personaje {i+1}: ").strip()
    pj_Attack = float(input(f"Ingrese la estadística de ataque de {pj_Name}: "))

    # Dentro del diccionario, cada héroe es una lista, dentro de esa lista, hay diccionarios, que están asociados al héroe.
    heroe[pj_Name] = {"Ataque": pj_Attack}

# Mostramos cada héroe creado con sus estadísticas.
print("\nHéroes creados:")
for nombre, estadisticas in heroe.items():
    print(f"Nombre: {nombre}")
    print(F"Estadísticas: {estadisticas}")
    print("-"*20)

print("Es momento de actualizar un héroe.")


# Aquí buscamos el héroe dentro del diccionario.
nombre_actualizar = input(f"\nIngresa el nombre del héroe que deseas actualizar: ")
if nombre_actualizar in heroe:
    print(f"\nEstadísticas actuales de \"{nombre_actualizar}\": {heroe[nombre_actualizar]}")
    nuevo_ataque = float(input(f"Ingrese el nuevo ataque para \"{nombre_actualizar}\": "))
    heroe[nombre_actualizar]["Ataque"] = nuevo_ataque
    print(f"\nACTUALIZADO: \"{nombre_actualizar}\" ahora tiene {nuevo_ataque} de ataque.")
else:
    print("Error: Ese héroe no existe en la lista.")
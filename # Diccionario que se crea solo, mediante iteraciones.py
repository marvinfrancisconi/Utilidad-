# Diccionario que se crea solo, mediante iteración.

# Crear un diccionario vacío.
diccionario = {}

# ¿Cuántas cosas quieres añadir?
cantidad = int(input("¿Cuántos alumnos quieres añadir? "))

# Iterar para la cantidad.
for i in range(cantidad):
    alumno = input(f"¿Quién es el alumno {i+1}? ").strip().capitalize()
    nota = input(f"¿Cuál es la nota del alumno {alumno}? ")
    print("-"*20)
    # Aquí es dónde se añadi al diccionario.
    diccionario[alumno] = nota

# Imprimirlo en un formato más legible.
for alumno, nota in diccionario.items():
    print(f"Alumno: {alumno}")
    print(f"Nota: {nota}")
    print("-"*20)
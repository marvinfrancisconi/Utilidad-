# Ordenamiento de datos en un diccionario.

# Digamos que te dan la siguiente información:
# 7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;‘
# Como ves, hay 4 valores antes de llegar a #Name, además separa los demás con ;;
# Vamos a ordenarlo para poder imprimirlo de una forma más legible.

data = "7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;"

# Primero dividimos la cadena en las partes separadas por ';;'
parts = data.split(';;')

# Inicializamos el diccionario
result = {}

# Recorremos las partes
for part in parts:
    if part != "":  # Verifica explícitamente que la parte no esté vacía
        numbers_part, name = part.split('#')
        numbers = list(map(float, numbers_part.split(',')))
        result[name] = numbers

# Ahora result contiene {'Ana': [7.8, 6.0, 4.5, 9.8], 'Miguel': [2.3, 3.4, 4.5, 2.1]}
curso = result

# Para calcular y mostrar el promedio de las notas
for estudiante, notas in curso.items():
    print(f"Estudiante: {estudiante}")
    print(f"Notas: {notas}")

    # Para calcular el promedio usamos sum() y len()
    # Redondeamos con round() a 2 décimas.
    promedio = round(sum(notas) / len(notas), 2)
    print(f"Promedio: {promedio}")
    print("-" * 20)

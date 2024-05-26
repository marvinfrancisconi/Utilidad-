# Ordenamiento de datos en un diccionario.

# Digamos que te dan la siguiente información:
# 7.8,6,4.5,9.8#Ana;;2.3,3.4,4.5,2.1#Miguel;;‘
# Como ves, hay 4 valores antes de llegar a #Name, además separa los demás con ;;
# Vamos a ordenarlo para poder imprimirlo de una forma más legible.

curso = {"Ana":[7.8,6,4.5,9.8],
         "Miguel":[2.3,3.4,4.5,2.1]}
 
# Para no hacer la división del promedio dentro de la lista, podemos crear otro código que sume estos valores y sea dividido por la cantidad de los mismos.
# Esto sería más útil en caso que la persona decida añadir más notas, y el código no sea modificado en lo absoluto.

for estudiante, notas in curso.items():
    print(f"Estudiante: {estudiante}")
    print(f"Notas: {notas}")

    # Para calcular el promedio usamos sum() y len()
    # Redondeamos con round() a 2 décimas.
    print(f"Promedio: {round((sum(notas)/len(notas)),2)}")
    print("-"*20)
    
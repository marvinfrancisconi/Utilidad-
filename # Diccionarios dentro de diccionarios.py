# Diccionarios dentro de diccionarios.

# Definimos un diccionario vacío. 
bigbaydata = {}

# Hagamos que la persona rellene el diccionario a su antojo.
# Preguntemos cuantos cursos quiere.
cantidad = int(input(("¿Cuántos cursos quieres crear? ")))

# Iteramos para crear cada curso
for i in range(1, cantidad + 1):
    # Nombre del curso, usamos "Curso" + número como clave
    curso_key = f"Curso {i}"
    
    # Inicializamos la estructura del curso
    # La primera línea está abriendo el dicci onario entero del Curso (i), para que sea rellenado uno a uno.
    bigbaydata[curso_key] = {
        "Nombre": input(f"Ingrese el nombre para {curso_key}: "),
        "Precio": float(input(f"Ingrese el precio para {curso_key}: ")),
        "Detalles": {
            "Profesor": input(f"Ingrese el nombre del profesor para {curso_key}: "),
            "Contacto": input(f"Ingrese el contacto del profesor para {curso_key}: "),
            # Para los alumnos, debido a que pueden ser varios, es mejor crear una lista.
            "Lista de alumnos totales": [],
            "Evaluación promedio": float(input(f"Ingrese la evaluación promedio para {curso_key}: "))
        }
    }
    
    # Pedimos cuántos alumnos quiere inscribir
    num_alumnos = int(input(f"¿Cuántos alumnos quiere inscribir en {curso_key}? "))
    
    # Pedimos los nombres de los alumnos uno por uno
    for j in range(num_alumnos):
        alumno = input(f"Ingrese el nombre del alumno {j+1} para {curso_key}: ")
        bigbaydata[curso_key]["Detalles"]["Lista de alumnos totales"].append(alumno)

# Mostramos el diccionario lleno de manera más sencilla
# Debido a que hay tres diccionarios, hay que hacer 3 for, para ir desglosando uno a uno, pero sin perder el orden.
# Es decir, 1 for, dentro de otro for, dentro de otro for, para desglosar cada diccionario.
for curso, detalles in bigbaydata.items():
    print(f"\n{curso}:")
    for key, value in detalles.items():
        # Para la llave detalles, hay que crear otro for.
        if key == "Detalles":
            print(f"{'-'*10} {key}:")
            for sub_key, sub_value in value.items():
                print(f"{'-'*15} {sub_key}: {sub_value}")
        else:
            print(f"{'-'*10} {key}: {value}\n")

# El diccionario perfectamente pudo haber sido estructurado de la siguiente manera:
#bigbaydata = {
#    "Curso": {
#        "Nombre": "",
#        "Precio": 0.0,
#        "Detalles": {
#            "Profesor": "",
#            "Contacto": "",
#            "Lista de alumnos totales": [],
#            "Evaluación promedio": 0.0
#        }
#    }
#}
# Así hubiese quedado como una variable, pero luego tienes que ir rellenando uno a uno utilizando la key del valor asociado.
# En mi opinión, iterar con for y colocando input en la estrucutura ya hecha, ahorra muchas líneas de código y es más legible.
# Puedes intentar hacerlo de esta manera, o como lo he hecho yo.
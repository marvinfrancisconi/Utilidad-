# Modificación de variables de un diccionario que ya existe.

# Esta vez, creamos un diccionario que contenga cosas, en este caso, días de la semana.
semana = {
    "Lunes": [],
    "Martes": ["Comprar víveres", "Pagar facturas"],
    "Miércoles": [],
    "Jueves": [],
    "Viernes": ["Llevar el carro al taller", "Ir al supermercado"],
    "Sábado": [],
    "Domingo": []
}

# Como los diccionarios tienen un par, porque cada  significa algo, puedes hacer que el signicado de esa variable sea múltiple, haciéndolo una lista.

# Recorramos la lista y mostremos al usuario.
print("Tareas pendientes: ")
for day, chores in semana.items():
    print(f"{day}: {chores}")
    print("-"*20)

# Revisemos un elemnto en particular del diccionario.
check_Day = input(f"¿Qué día quieres ver? ").strip().capitalize()
if check_Day in semana:
    if semana[check_Day]:
        print(f"Tareas para {check_Day}: ")
        for chores in semana[check_Day]:
            print(f"{chores}")
    
    # Si no hay tareas ese día, preguntemos si quiere añadir alguna.
    else:
        print(f"\nVaya, parece que no hay tareas para el día {check_Day}")
        crear_Tarea = input("\n¿Quieres hacer una tarea? (y/n)").strip().lower()
        if crear_Tarea == "y":
            tarea_Nueva = input(f"\nBueno, ingresa la tarea: ").strip().capitalize()
            
            # Aquí es donde se añade la tarea, con el clásico .append()
            semana[check_Day].append(tarea_Nueva)
            print(f"Tarea \"{tarea_Nueva}\" agregada al día {check_Day}.")
            
            # Imprimos el diccionario actualizado.
            print("Tareas pendientes: ")
            for day, chores in semana.items():
                print(f"{day}: {chores}")
                print("-"*20)
else:
    print("Día no válido.")

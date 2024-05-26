# Código para calcular edades.
# Puede ser útil para diferentes situaciones en los que se requiere saber cuánto tiempo ha pasado desde una fecha específica hasta el día presente.
import datetime

# Solicita al usuario que ingrese su fecha de nacimiento en formato YYYY/MM/DD
fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (YYYY/MM/DD): ")

# Convierte la cadena a un objeto datetime, asegurando también que se ingresen números.
try:
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%Y/%m/%d")
    
    # Obtiene la fecha actual
    fecha_actual = datetime.datetime.now()
    
    # Calcula la diferencia en años, meses y días
    edad_years = fecha_actual.year - fecha_nacimiento.year
    edad_months = fecha_actual.month - fecha_nacimiento.month
    edad_days = fecha_actual.day - fecha_nacimiento.day

    # Ajusta si el día de nacimiento aún no ha ocurrido en el año actual
    if edad_days < 0:
        edad_months -= 1
        # Calcula el número de días en el mes anterior
        ultimo_dia_mes_anterior = (fecha_actual.replace(day=1) - datetime.timedelta(days=1)).day
        edad_days += ultimo_dia_mes_anterior

    # Ajusta si el mes de nacimiento aún no ha ocurrido en el año actual
    if edad_months < 0:
        edad_years -= 1
        edad_months += 12

    # Muestra el resultado
    print(f"Tienes {edad_years} años, {edad_months} meses y {edad_days} días.")
except ValueError:
    print("Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato YYYY/MM/DD.")

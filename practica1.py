from datetime import datetime

def pedir_dato(mensaje):
    dato = ""
    while not dato.strip():
        dato = input(mensaje).strip()
        if not dato:
            print("Por favor, ingrese un valor.")
    return dato

def pedir_fecha_nacimiento():
    while True:
        fecha_str = pedir_dato("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Formato incorrecto. Usa YYYY-MM-DD.")

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

nombre = pedir_dato("Introduce tu nombre: ")
fecha_nacimiento = pedir_fecha_nacimiento()
edad = calcular_edad(fecha_nacimiento)

if edad < 0 or edad > 100:
    print("Edad fuera de rango válido (0-100 años).")
else:
    if edad < 18:
        rango = "menor de edad"
    elif edad <= 65:
        rango = "adulto"
    else:
        rango = "anciano"
    print(f"{nombre}, tienes {edad} años y eres {rango}.")
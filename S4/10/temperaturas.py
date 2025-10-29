# temperaturas.py
# Pide una temperatura en °C, la convierte a Kelvin o Fahrenheit según la elección
# y dice si está por encima/por debajo de la temperatura media de España
# además indica si es una temperatura en la que se puede vivir (rango práctico).
# temperaturas.py
# Pide una temperatura en °C, la convierte a Kelvin o Fahrenheit según la elección
# y dice si está por encima/por debajo de la temperatura media de España
# además indica si es una temperatura en la que se puede vivir (rango práctico).

def main():
    # Temperatura media aproximada de España en °C
    media_espana = 15.0

    # Lectura de la temperatura en Celsius
    
    entrada = input("Introduce la temperatura en grados Celsius (ej: 23.5): ").strip()
    try:
            c = float(entrada.replace(",", "."))
    except ValueError:
            print("Valor no válido. Introduce un número válido.")

    # Elección del tipo de conversión
    
    eleccion = input("Convertir a (K)elvin o (F)ahrenheit? [K/F]: ").strip().upper()
    if eleccion not in ("K", "F"):
        print("Opción no válida. Escribe 'K' para Kelvin o 'F' para Fahrenheit.")
        return

    # Conversión
    if eleccion == "K":
        convertido = c + 273.15
        unidad = "K"
    else:  # "F"
        convertido = c * 9/5 + 32
        unidad = "°F"

    print(f"\nResultado: {convertido:.2f} {unidad} (desde {c:.2f} °C)")

    # Comparación con la media de España
    if c > media_espana:
        print(f"La temperatura está por encima de la media de España ({media_espana} °C).")
    elif c < media_espana:
        print(f"La temperatura está por debajo de la media de España ({media_espana} °C).")
    else:
        print(f"La temperatura es igual a la media de España ({media_espana} °C).")

    # Evaluación de habitabilidad/practicidad
    # Definiciones:
    # - Rango "se puede vivir": entre -20 °C y 50 °C (supervivencia con medios básicos)
    # - Rango "cómodo": entre 10 °C y 35 °C
    if -20.0 <= c <= 50.0:
        print("Es una temperatura en la que se puede vivir.")
        if 10.0 <= c <= 35.0:
            print("Además, es un rango cómodo para la vida diaria.")
        else:
            print("No es especialmente cómoda, pero es posible vivir con medidas adecuadas.")
    else:
        print("No es una temperatura adecuada para vivir sin medidas extremas (riesgo para la salud).")

if __name__ == "__main__":
    main()

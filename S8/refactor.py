def programa():
    alumnos = []
    
    try:
        n = int(input("¿Cuántos alumnos? "))
        if n <= 0:
            print("El número de alumnos debe ser mayor que 0.")
            return  # Salir de la función sin continuar
    except ValueError:
        print("Error: Debes introducir un número entero.")
        return

    # Pedir notas
    for i in range(n):
        while True:
            try:
                nota = float(input(f"Nota del alumno {i + 1}: "))
                if 0 <= nota <= 10:
                    alumnos.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Error: introduce un número válido.")

    # Calcular media (ya sabemos que n > 0, así que no hay riesgo de división por 0)
    media = sum(alumnos) / len(alumnos)
    print(f"\nMedia de la clase: {media:.2f}")

    print("Aprobados:")
    aprobados = [nota for nota in alumnos if nota >= 5]
    if aprobados:
        for nota in aprobados:
            print(nota)
    else:
        print("Ninguno.")


def main():
    programa()


if __name__ == "__main__":
    main()
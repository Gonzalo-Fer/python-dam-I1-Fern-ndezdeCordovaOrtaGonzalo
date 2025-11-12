# ---------------- CONTROL DE TAREAS ----------------
import datetime  # Módulo estándar para manejar fechas y horas

# ---------------- FUNCIONES ----------------

def agregar_tarea(tareas, descripcion):
    """
    Agrega una tarea nueva con la fecha actual.
    Parámetros:
        tareas (list): lista actual de tareas
        descripcion (str): texto descriptivo de la tarea
    Retorna:
        list: lista de tareas actualizada
    """
    fecha = datetime.date.today()  # Fecha de hoy
    tarea = {"descripcion": descripcion, "fecha": fecha, "completada": False}
    tareas.append(tarea)
    return tareas


def mostrar_tareas(tareas):
    """
    Muestra todas las tareas con su estado.
    Parámetros:
        tareas (list): lista de tareas
    Retorna:
        int: número de tareas mostradas
    """
    if not tareas:
        print("No hay tareas registradas.")
        return 0

    print("\n=== LISTA DE TAREAS ===")
    for i, t in enumerate(tareas):
        estado = "✅" if t["completada"] else "❌"
        print(f"{i}. {t['descripcion']} (Fecha: {t['fecha']}) - {estado}")
    return len(tareas)


def completar_tarea(tareas, indice):
    """
    Marca una tarea como completada según el índice.
    Parámetros:
        tareas (list): lista de tareas
        indice (int): posición de la tarea en la lista
    Retorna:
        bool: True si se completó correctamente, False si hubo error
    """
    try:
        tareas[indice]["completada"] = True
        return True
    except IndexError:
        print("Error: índice fuera de rango.")
        return False


# ---------------- PROGRAMA PRINCIPAL ----------------

def main():
    tareas = []
    while True:
        print("\n--- CONTROL DE TAREAS ---")
        print("1. Añadir tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Error: introduce un número válido.")
            continue

        if opcion == 1:
            descripcion = input("Descripción de la tarea: ")
            tareas = agregar_tarea(tareas, descripcion)
            print("Tarea añadida correctamente.")

        elif opcion == 2:
            mostrar_tareas(tareas)

        elif opcion == 3:
            mostrar_tareas(tareas)
            try:
                idx = int(input("Introduce el número de la tarea a completar: "))
                if completar_tarea(tareas, idx):
                    print("Tarea marcada como completada.")
            except ValueError:
                print("Error: introduce un número válido.")

        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()

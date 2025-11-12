# Estructura para almacenar los datos de las asignaturas
asignaturas = {}

def agregar_asignatura(nombre, num_examenes, notas):
    """Función para agregar una nueva asignatura"""
    try:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la asignatura debe ser una cadena no vacía")
        if not isinstance(num_examenes, int) or num_examenes <= 0:
            raise ValueError("El número de exámenes debe ser un entero positivo")
        if not isinstance(notas, list) or len(notas) != num_examenes:
            raise ValueError("Las notas deben ser una lista y coincidir con el número de exámenes")
        
        media = sum(notas) / len(notas)
        asignaturas[nombre.lower()] = {
            'num_examenes': num_examenes,
            'notas': notas,
            'media': round(media, 2)
        }
        print(f"Asignatura {nombre} agregada correctamente")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def buscar_asignatura(nombre):
    """Función para buscar una asignatura"""
    try:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de búsqueda debe ser una cadena no vacía")
        
        nombre = nombre.lower()
        if nombre in asignaturas:
            datos = asignaturas[nombre]
            print(f"\nDatos de la asignatura {nombre.capitalize()}:")
            print(f"Número de exámenes: {datos['num_examenes']}")
            print(f"Notas: {datos['notas']}")
            print(f"Media: {datos['media']}")
        else:
            print(f"No se encontró la asignatura {nombre}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    agregar_asignatura("Matemáticas", 3, [7.5, 8.0, 6.5])
    agregar_asignatura("Programación", 2, [9.0, 8.5])
    agregar_asignatura("Física", 4, [6.0, 7.0, 7.5, 8.0])

    # Buscar asignaturas
    buscar_asignatura("Matemáticas")
    buscar_asignatura("Programación")
    buscar_asignatura("Historia")  # Asignatura que no existe
    buscar_asignatura("Física")
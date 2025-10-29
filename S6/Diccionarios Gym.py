# Sistema sencillo de gestión de un gimnasio usando diccionarios
# Archivo: Diccionarios Gym.py
# No se usan funciones ni módulos externos: todo está en un solo script.
# Comentarios explican cada bloque de forma simple.

# Diccionario principal: la clave es el ID del socio (string) y el valor es otro diccionario con campos.
socios = {
    "001": {"nombre": "Ana Perez", "edad": 28, "tipo": "Mensual", "asistencias": 12, "peso": 63.5},
    "002": {"nombre": "Luis Gomez", "edad": 35, "tipo": "Anual", "asistencias": 30, "peso": 82.0},
}

# Bucle principal del programa: muestra un menú y permite insertar, modificar, eliminar, listar y calcular métricas.
while True:
    print("\n--- GESTIÓN GIMNASIO ---")
    print("1. Insertar socio")
    print("2. Modificar socio")
    print("3. Eliminar socio")
    print("4. Listar socios (recorrer claves y valores)")
    print("5. Calcular métricas (media, mínimos, máximos)")
    print("6. Salir")
    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
        # Insertar un registro nuevo
        nuevo_id = input("ID nuevo (ej. 003): ").strip()
        if nuevo_id in socios:
            print("Ya existe un socio con ese ID.")
        else:
            nombre = input("Nombre: ").strip()
            try:
                edad = int(input("Edad: ").strip())
            except:
                print("Edad inválida, se asigna 0.")
                edad = 0
            tipo = input("Tipo de membresía (Mensual/Anual): ").strip()
            try:
                asistencias = int(input("Asistencias registradas: ").strip())
            except:
                print("Asistencias inválidas, se asigna 0.")
                asistencias = 0
            try:
                peso = float(input("Peso (kg): ").strip())
            except:
                print("Peso inválido, se asigna 0.0.")
                peso = 0.0
            # Se añade al diccionario principal
            socios[nuevo_id] = {"nombre": nombre, "edad": edad, "tipo": tipo, "asistencias": asistencias, "peso": peso}
            print(f"Socio {nuevo_id} insertado.")

    elif opcion == "2":
        # Modificar un registro existente
        id_mod = input("ID del socio a modificar: ").strip()
        if id_mod not in socios:
            print("ID no encontrado.")
        else:
            # Mostrar datos actuales
            print("Datos actuales:", socios[id_mod])
            print("Campos: nombre, edad, tipo, asistencias, peso")
            campo = input("¿Qué campo quieres modificar? ").strip().lower()
            if campo not in ("nombre", "edad", "tipo", "asistencias", "peso"):
                print("Campo no válido.")
            else:
                nuevo_val = input("Nuevo valor: ").strip()
                # Convertir tipos según el campo
                if campo == "edad":
                    try:
                        socios[id_mod][campo] = int(nuevo_val)
                    except:
                        print("Valor inválido para edad; no se cambia.")
                elif campo == "asistencias":
                    try:
                        socios[id_mod][campo] = int(nuevo_val)
                    except:
                        print("Valor inválido para asistencias; no se cambia.")
                elif campo == "peso":
                    try:
                        socios[id_mod][campo] = float(nuevo_val)
                    except:
                        print("Valor inválido para peso; no se cambia.")
                else:
                    socios[id_mod][campo] = nuevo_val
                print("Registro actualizado:", socios[id_mod])

    elif opcion == "3":
        # Eliminar un registro
        id_del = input("ID del socio a eliminar: ").strip()
        if id_del in socios:
            confirm = input(f"Confirma eliminar socio {id_del} (s/n): ").strip().lower()
            if confirm == "s":
                socios.pop(id_del)
                print("Socio eliminado.")
            else:
                print("Operación cancelada.")
        else:
            print("ID no encontrado.")

    elif opcion == "4":
        # Recorrer claves y valores con un bucle
        if not socios:
            print("No hay socios registrados.")
        else:
            print("\nListado de socios (ID -> datos):")
            # Usamos items() para recorrer claves y valores
            for id_socio, datos in socios.items():
                # Mostrar cada clave (ID) y su diccionario de valores
                print(f"ID: {id_socio}")
                # Recorrer los pares dentro del diccionario de cada socio
                for campo, valor in datos.items():
                    print(f"  {campo}: {valor}")
                print("-" * 20)

    elif opcion == "5":
        # Calcular métricas: media de edad, media de asistencias, mínimo y máximo de peso
        if not socios:
            print("No hay datos para calcular métricas.")
        else:
            edades = [d["edad"] for d in socios.values()]
            asistencias = [d["asistencias"] for d in socios.values()]
            pesos = [d["peso"] for d in socios.values()]

            # Media (promedio)
            media_edad = sum(edades) / len(edades) if edades else 0
            media_asist = sum(asistencias) / len(asistencias) if asistencias else 0.0

            # Mínimos y máximos
            min_peso = min(pesos) if pesos else None
            max_peso = max(pesos) if pesos else None

            print(f"Media de edad: {media_edad:.2f}")
            print(f"Media de asistencias: {media_asist:.2f}")
            if min_peso is not None:
                print(f"Peso mínimo: {min_peso:.1f} kg")
                print(f"Peso máximo: {max_peso:.1f} kg")

            # Ejemplo adicional: identificar socio con más asistencias
            mas_asistencias = max(asistencias) if asistencias else None
            if mas_asistencias is not None:
                # Buscar el primer socio que tenga ese número de asistencias
                for id_socio, datos in socios.items():
                    if datos["asistencias"] == mas_asistencias:
                        print(f"Socio con más asistencias: {id_socio} - {datos['nombre']} ({mas_asistencias})")
                        break

    elif opcion == "6":
        print("Saliendo del sistema.")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
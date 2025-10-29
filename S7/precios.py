# precios.py
# Llama a las funciones de auxprecios.py y muestra resultados de ejemplo.

try:
    from auxprecios import (
        calcular_promedio,
        encontrar_precio_max,
        encontrar_precio_min,
        contar_precios_mayores_que,
        filtrar_precios_rango,
    )
except ImportError as e:
    raise ImportError(
        "No se pudo importar auxprecios. Asegúrate de que usxprecios.py esté en el mismo directorio."
    ) from e


def main():
    precios = [120.5, 99.99, 250.0, 75.0, 150.0, 99.99, 200.0]

    try:
        promedio = calcular_promedio(precios)
        precio_max = encontrar_precio_max(precios)
        precio_min = encontrar_precio_min(precios)
        mayores_a_100 = contar_precios_mayores_que(precios, 100)
        entre_90_y_160 = filtrar_precios_rango(precios, 90, 160)
    except Exception as e:
        print("Error al usar las funciones de usxprecios:", e)
        return

    print("Lista de precios:", precios)
    print("Promedio:", promedio)
    print("Precio máximo:", precio_max)
    print("Precio mínimo:", precio_min)
    print("Cantidad de precios > 100:", mayores_a_100)
    print("Precios entre 90 y 160:", entre_90_y_160)


if __name__ == "__main__":
    main()
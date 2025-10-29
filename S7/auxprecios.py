def calcular_promedio(precios):
    """Calcula el promedio de una lista de precios"""
    if not precios:
        return 0
    return sum(precios) / len(precios)

def encontrar_precio_max(precios):
    """Encuentra el precio más alto en la lista"""
    if not precios:
        return 0
    return max(precios)

def encontrar_precio_min(precios):
    """Encuentra el precio más bajo en la lista"""
    if not precios:
        return 0
    return min(precios)

def contar_precios_mayores_que(precios, limite):
    """Cuenta cuántos precios son mayores que un límite dado"""
    return sum(1 for precio in precios if precio > limite)

def filtrar_precios_rango(precios, min_precio, max_precio):
    """Filtra precios que están dentro de un rango específico"""
    return [precio for precio in precios if min_precio <= precio <= max_precio]

# Solo si se ejecuta como script principal
if __name__ == "__main__":
    # Ejemplo de uso
    precios_prueba = [10.5, 20.3, 15.2, 30.5, 25.8]
    print(f"Promedio: {calcular_promedio(precios_prueba)}")
    print(f"Precio máximo: {encontrar_precio_max(precios_prueba)}")
    print(f"Precio mínimo: {encontrar_precio_min(precios_prueba)}")
from collections import Counter
import re
"""
# "  3.14  ".strip() -> "3.14". Esto evita errores al convertir la cadena a float eliminando espacios.
"""

#!/usr/bin/env python3

# Patrón que acepta enteros, floats (con o sin parte entera) y notación científica,
# separados por comas opcionalmente con espacios alrededor.
_NUM_LIST_RE = re.compile(
    r'^\s*[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'
    r'(?:\s*,\s*[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?\s*)*$'
)

def validar_entrada(entrada: str) -> bool:
    """Devuelve True si entrada es una lista válida de números separados por comas."""
    if not entrada or entrada.strip() == "":
        return False
    return bool(_NUM_LIST_RE.match(entrada))

def pedir_numeros():
    while True:
        entrada = input("Introduce una lista de números separados por comas: ").strip()
        if not entrada:
            print("Entrada vacía. Inténtalo de nuevo.")
            continue
        partes = [p.strip() for p in entrada.split(",") if p.strip() != ""]
        if not partes:
            print("No se detectaron números. Inténtalo de nuevo.")
            continue
        try:
            nums = [float(p) for p in partes]
            return nums
        except ValueError:
            print("Uno o más valores no son números válidos. Inténtalo de nuevo.")

def resumen(nums):
    total = sum(nums)
    media = total / len(nums)
    maximo = max(nums)
    cont = Counter(nums)
    repetidos = {n: c for n, c in cont.items() if c > 1}
    # contar cuántas veces aparece cada número (incluye apariciones únicas)
    conteos = dict(cont)
    # si quieres mantener sólo los repetidos deja la línea anterior y comenta la siguiente
    repetidos = conteos
    return total, media, maximo, repetidos

def formato_num(n):
    # Muestra floats de forma compacta (sin ceros innecesarios)
    return f"{n:g}"

def main():
    nums = pedir_numeros()
    total, media, maximo, repetidos = resumen(nums)
    print()
    print(f"Suma: {total}")
    print(f"Media: {media}")
    print(f"Máximo: {formato_num(maximo)}")
    if repetidos:
        print("Números repetidos:")
        for n, c in sorted(repetidos.items(), key=lambda x: x[0]):
            print(f"  {formato_num(n)} -> {c} veces")
    else:
        print("No hay números repetidos.")

if __name__ == "__main__":
    main()
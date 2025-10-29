# Cadenas.py
# Pide una cadena y cuenta vocales, consonantes, mayúsculas, minúsculas y total de caracteres.
# Además muestra la cadena al revés.

def analizar_cadena(s: str) -> dict:
    vocales = set("aeiouáéíóúü")
    counts = {
        "vocales": 0,
        "consonantes": 0,
        "mayusculas": 0,
        "minusculas": 0,
        "total": len(s),
        "invertida": s[::-1],
    }

    for ch in s:
        if ch.isalpha():
            if ch.lower() in vocales:
                counts["vocales"] += 1
            else:
                counts["consonantes"] += 1

        if ch.isupper():
            counts["mayusculas"] += 1
        elif ch.islower():
            counts["minusculas"] += 1

    return counts


if __name__ == "__main__":
    entrada = input("Introduce una cadena de caracteres: ")
    resultado = analizar_cadena(entrada)

    print("\nResultados:")
    print(f"Cadena: {entrada}")
    print(f"Cadena invertida: {resultado['invertida']}")
    print(f"Total de caracteres: {resultado['total']}")
    print(f"Vocales: {resultado['vocales']}")
    print(f"Consonantes: {resultado['consonantes']}")
    print(f"Mayúsculas: {resultado['mayusculas']}")
    print(f"Minúsculas: {resultado['minusculas']}")
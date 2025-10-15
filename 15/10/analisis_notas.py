from collections import Counter

#!/usr/bin/env python3
# analisis_notas.py


# Este programa pide una lista de calificaciones (números reales entre 0 y 10)
# esta funcion pide la lista de notas y las valida separandolas por la coma para quedarnos solo con los numeros
# y las convierte a float, si hay algun valor no convertible a float lo descarta y avisa al usuario
# si no hay ningun valor valido vuelve a pedir la lista

def pedir_notas():
        while True:
            entrada = input("Introduce calificaciones separadas por comas: ").strip()
            if ',' not in entrada:
                print("La lista debe estar separada por comas. Intenta de nuevo.")
                continue

            partes = [p.strip() for p in entrada.split(',')]
            validas = []
            descartadas = []

            for p in partes:
                if p == '':
                    descartadas.append('(vacío)')
                    continue
                try:
                    v = float(p)
                    if 0 <= v <= 10:
                        validas.append(v)
                    else:
                        descartadas.append(p)
                except ValueError:
                    descartadas.append(p)

            if descartadas:
                print("Se descartaron los valores no válidos:", ", ".join(descartadas))

            if validas:
                return validas

            print("No se obtuvo ninguna nota válida. Inténtalo de nuevo.")


def calcular_modal(notas):
        conteo = Counter(notas)
        max_c = max(conteo.values())
        modos = sorted([nota for nota, cnt in conteo.items() if cnt == max_c])
        if len(modos) == 1:
            return modos[0]
        return modos  # puede devolver lista si hay empate


def main():
        # Recogemos las notas y medimos la longitud para sacar la media, minimo y maximo se hace con las funciones nativas de python
        # para contar los aprobados y sobresalientes usamos una comprension de listas y los porcentajes se sacan con una regla de 3
        # la moda se calcula con la funcion calcular_modal
        notas = pedir_notas()

        total = len(notas)
        media = sum(notas) / total
        minima = min(notas)
        maxima = max(notas)
        aprobados = sum(1 for n in notas if n >= 5)
        sobresalientes = sum(1 for n in notas if n >= 9)
        pct_aprobados = aprobados / total * 100
        pct_sobres = sobresalientes / total * 100
        moda = calcular_modal(notas)

        idx_max = notas.index(maxima)      # índice 0-based
        idx_min = notas.index(minima)

        print(f"\nNúmero total de notas: {total}")
        print(f"Media: {media:.2f}")
        print(f"Nota mínima: {minima:.2f} (posición index: {idx_min:.2f}, posición humana: {idx_min + 1})")
        print(f"Nota máxima: {maxima:.2f} (posición index: {idx_max:.2f}, posición humana: {idx_max + 1})")
        print(f"Porcentaje de aprobados (>=5): {pct_aprobados:.2f}%")
        print(f"Porcentaje de sobresalientes (>=9): {pct_sobres:.2f}%")

        if isinstance(moda, list):
            print("Nota modal (varias):", ", ".join(f"{m:.2f}" for m in moda))
        else:
            print(f"Nota modal: {moda:.2f}")

        # Mensaje final según la media
        if media < 5:
            print("Necesita refuerzo")
        elif 5 <= media <= 7.9:
            print("Nivel medio")
        else:  # media > 7.9 (se considera nivel excelente a partir de 8.0)
            print("Nivel excelente")


if __name__ == "__main__":
        main()

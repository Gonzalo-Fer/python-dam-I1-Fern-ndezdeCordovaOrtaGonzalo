#!/usr/bin/env python3
# ecp_io.py
# Pide 3 números al usuario, calcula suma, media, máximo y muestra cuáles son pares/impares.

def pedir_enteros(n=3):
    nums = []
    for i in range(1, n+1):
        while True:
            try:
                v = int(input(f"Introduce el número {i}: ").strip())
                nums.append(v)
                break
            except ValueError:
                print("Entrada no válida. Por favor introduce un número entero.")
    return nums

def es_par(x):
    return x % 2 == 0

def main():
    nums = pedir_enteros(3)
    suma = sum(nums)
    media = suma / len(nums)
    maxima = max(nums)

    print("\nResultados:")
    print(f"Suma: {suma}")
    print(f"Media: {media}")
    print(f"Número máximo: {maxima}\n")

    for i, v in enumerate(nums, start=1):
        tipo = "par" if es_par(v) else "impar"
        print(f"Número {i} ({v}) -> {tipo}")

if __name__ == "__main__":
    main()
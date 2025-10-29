def main():
    try:
        n = int(input("Introduce un número entero: ").strip())
    except ValueError:
        print("Entrada no válida. Introduce un entero.")
        return

    if n < 2:
        print(f"El número {n} no es primo.")
        return
    if n == 2:
        print(f"El número {n} es primo.")
        return
    if n % 2 == 0:
        print(f"El número {n} no es primo.")
        return

    i = 3
    while i * i <= n:
        if n % i == 0:
            print(f"El número {n} no es primo.")
            return
        i += 2

    print(f"El número {n} es primo.")

if __name__ == "__main__":
    main()

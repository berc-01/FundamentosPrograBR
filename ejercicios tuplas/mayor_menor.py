def main():
    tupla = (10, 4, 3, 5, 6, 2, 1, 7, 8, 9)
    print(f"La tupla es: {tupla}")

    mayor_menor = mayor_y_menor(tupla)
    print(f"EL número mayor y el número menor de la tupla es: {mayor_menor}")

def mayor_y_menor(tupla):
    return (max(tupla), min(tupla))

if __name__ == "__main__":
    main()
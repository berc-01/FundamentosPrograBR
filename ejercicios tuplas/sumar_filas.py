def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matriz")
    for fila in matriz:
        print(fila)

    resultados = sumar_filas(matriz)
    print(f"La suma de cada fila es: {resultados}")

def sumar_filas(matriz):
    return [sum(fila) for fila in matriz]
    

if __name__ == "__main__":
    main()
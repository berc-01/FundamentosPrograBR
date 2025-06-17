def main():
    lista_notas = [2.4, 3.0, 7.0, 6.4, 5.5, 6.8]
    promedio = promedio_notas(lista_notas)
    print(f"Las notas ingresadas son: {lista_notas} \nEl promedio del curso es: {round(promedio, 2)}") #También se puede hacer con :.2f

def promedio_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

if __name__ == "__main__":
    main()
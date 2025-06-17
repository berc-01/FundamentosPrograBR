def main():
    lista_palabras = ["hola", "uno", "dos", "tres", "hola"]
    resultado = contar_ocurrencias(lista_palabras)
    print(f"El número de palabras dentro de la lista es: {resultado}")

def contar_ocurrencias(lista_palabras):
    conteo = {}
    for palabra in lista_palabras:
        conteo[palabra] = conteo.get(palabra , 0) + 1
    return conteo

if __name__ == "__main__":
    main()
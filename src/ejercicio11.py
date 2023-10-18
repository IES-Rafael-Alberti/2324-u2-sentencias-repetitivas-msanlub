#Escribir un programa que pida al usuario una palabra y luego muestre
#por pantalla una a una las letras de la palabra introducida empezando por la última.

def palabraInvertida(palabra:str) -> str:
    '''función que transforma letra a letra la palabra al revés'''
    return palabra[::-1]

if __name__=="__main__":
#entrada
    palabra = str(input("Escribe una palabra: "))

#proceso
    invertida = palabraInvertida(palabra)

#salida
    for letra in invertida:
        print(letra)

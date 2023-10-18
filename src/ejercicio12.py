#Escribir un programa en el que se pregunte al usuario por una frase 
#y una letra, y muestre por pantalla el número de veces que aparece la 
#letra en la frase.

def conteoFrase(frase:str,letra:str) -> int:
    '''función que da el número de veces que aparede la letra en la frase'''
    contador = 0
    for letra in frase:
        if letra == letra:
            contador += 1


if __name__=="__main__":
#entrada
    frase = str(input("Escribe una frase: "))
    letra = str(input("Escribe la letra que quieres contar en la frase: "))

#proceso
    conteo = conteoFrase(frase,letra)

#salida
    print(conteo)
#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def recorridoFrase(frase:str,letra:str) ->str:
    '''función que recorre la frase caracter por caracter'''
    caracteres = []
    for caracter in frase:
        if caracter != letra:
            False
        else:
            caracteres.append(caracter)
    return caracteres

if __name__=="__main__":
    #entrada
    frase = input("Escribe una frase: ")
    letra = input("Ahora escribe la letra que quieres comprobar: ")

    #proceso
    coincidencia = recorridoFrase(frase,letra)
    
    #salida
    if coincidencia == False:
        print("No existe coincidencia")
    else:
        print(coincidencia)
    

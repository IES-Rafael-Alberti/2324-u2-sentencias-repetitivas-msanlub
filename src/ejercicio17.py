#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def separar(numero:int) -> int:
    '''función que realiza la suma de los números que componen el número'''
    numeros = 0
    while numero > 0:
        numeros= numeros + numero%10
        numero = numero//10
    return numeros

if __name__=="__main__":
    #entrada
    numero = int(input("Escribe un número positivo: "))
    while numero < 0:
        numero = int(input("Error, escribe un número positivo: "))
    
    #proceso
    resultado = separar(numero)

    #salida
    print(resultado)
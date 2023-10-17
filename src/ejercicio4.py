#Escribir un programa que pida al usuario un 
#número entero positivo y muestre por pantalla la cuenta atrás 
#desde ese número hasta cero separados por comas.

def listaEntero(entero:int) -> int:
    '''función que da el resultado de la lista desde 0 hasta entero'''
    numeros = []
    for numero in range(entero,-1,-1):
        numeros.append(numero)
    return numeros 

if __name__=="__main__":
#entrada
    entero = int(input("Escribe un numero: "))
#proceso
    lista = listaEntero(entero)
#salida
    print(lista)
#Escribir un programa que pida al usuario un número entero y muestre
#por pantalla si es un número primo o no.

def numPrimo(numero:int) -> int:
    '''función que calcula si es primo o no'''
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True
    
if __name__=="__main__":
#entrada
    numero = int(input("Escribe un número: "))

#proceso
    primo = numPrimo(numero)

#salida
    if numPrimo(numero) is False:
        print("No es primo.")
    else:
        print("Es primo.")
    

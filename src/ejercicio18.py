#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

def suma(numero:int) -> int:
    '''función que realiza la suma de los números que componen el número'''
    numeros = 0
    while numero > 0:
        numeros= numeros + numero%10
        numero = numero//10
    return numeros

def calculoPar(total):
    '''función que calcula la cantidad de números par'''
    paridad = 0
    while total == %2

if __name__=="__main__":
    #entrada
    numero = int(input("Ingresa un número entero positivo: "))

    #proceso
    total = suma(numero)
    par = calculoPar(total)
    
    #salida
    if total >= 0:
        print(total)
    else:
        print("El total de números pares es: " + str(par))
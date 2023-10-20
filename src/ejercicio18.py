#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

def suma(numero:int) -> int:
    '''función que realiza la suma de los números que componen el número'''
    numeros = 0
    while numero > 0:
        numeros= numeros + numero%10
        numero = numero//10
    return numeros
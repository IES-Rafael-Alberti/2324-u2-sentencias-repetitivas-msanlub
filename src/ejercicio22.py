#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

def numeroImpar(numero:int) -> int:
    '''función que da la serie de numero impares'''
    impares = []
    for n in range(numero):
        if n % 2 != 0:
            impares.append(n)
    return impares

def numeroPar(numero:int) -> int:
    '''función que da la serie de numero impares'''
    pares = []
    for n in range(numero):
        if n % 2 != 0:
            pares.append(n)
    return pares

if __name__=="__main__":
    #entrada
        numero = int(input("Escribe un numero: "))
        
    #proceso
        impar = numeroImpar(numero)
        par = numeroPar(numero)
        
    #salida
        if numero == impar:
            print("El número es impar")
        elif numero == par:
            print("El número es par")
            
        print("El total de números par es: " + str(list.count(par)) + ",el número de impares es: " + str(list.count(impar)))
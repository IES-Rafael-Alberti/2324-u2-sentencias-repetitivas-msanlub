#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

def numeroParidad(numero:int) -> int:
    '''función que da la serie de numero impares'''
    if numero % 2 != 0:
        return True
    else:
        return False

if __name__=="__main__":
    numero = 1
    impares = []
    pares = []
    while numero != 0:
        #entrada
        numero = int(input("Escribe un numero: "))
        
        #proceso
        if numeroParidad(numero):
            impares.append(numero)
        else:
            pares.append(numero)

    #salida
    print("El total de números par es: " + str(len(pares)) + ",el número de impares es: " + str(len(impares)))
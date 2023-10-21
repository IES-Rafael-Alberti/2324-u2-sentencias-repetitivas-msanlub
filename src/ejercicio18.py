#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

pares = []

def guardarNumeros(numero:int,pares:list) ->list:
    '''función que acumula los números ingresados y los va sumando'''
    bolsa = 0
    while numero != -1:
        if numero > 0:
            bolsa = bolsa + numero
            print(bolsa)
            if numero%2 == 0:
                pares.append(numero)
            numero = int(input("Ingresa otro número entero positivo: "))

if __name__=="__main__":
    #entrada
    numero = int(input("Ingresa un número entero positivo: "))

    #proceso
    conjuntoNumeros = guardarNumeros(numero,pares)

    #salida
    print("Los números pares ingresados fueron: " + str(pares))

#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def suma(numero:int) -> int:
    '''función que suma los numeros introducidos hasta que se escriba 0'''
    n = 0
    while numero > 0:
        n= n + numero
        if numero == 0:
            break
    return n

if __name__=="__main__":
    #entrada
    numero = int(input("Escribe un número: "))

    #procedimiento
    sumatorio = suma(numero)
    
    #salida
    print("La suma de todos los número es: " + str(sumatorio))
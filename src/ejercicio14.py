#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def listaNumeros(numero:int) -> int:
    '''función que añade los numeros enteros introducidos hasta que se escriba 0'''
    lista = []
    while numero != 0:
        lista.append(numero)
        numero = int(input("ingrese otro numero entero: "))
    return lista

if __name__=="__main__":
    #entrada
    numero = int(input("Escribe un número: "))

    #procedimiento
    sumatorio = listaNumeros(numero)
    
    #salida
    print("La suma de todos los número es: " + str(sum(sumatorio)))

#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

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
    numeroMayor = max(listaNumeros(numero))

    #salida
    print("El número mayor es: " + str(numeroMayor))
#Escribir un programa que pida al usuario un número entero y
#muestre por pantalla un triángulo rectángulo como el de más abajo.

def calculoTriangulo(numero:int):
    '''función que repite el numero para completar triangulo'''
    for i in range(1, numero+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")

if __name__=="__main__":
#entrada
    numero = int(input("Escribe un número entero: "))

#proceso
    triangulo = calculoTriangulo(numero)

#salida
    
#Escribir un programa que pida al usuario un número entero y
#muestre por pantalla un triángulo rectángulo como el de más abajo,
#de altura el número introducido.


def calculoTriangulo(numero:int):
    '''función que repite el numero para completar triangulo'''
    cantidades = []
    for n in range(numero):
        cantidad = "*" * (n+1)
        cantidades.append(cantidad)
    return cantidades
    
if __name__=="__main__":
#entrada
    numero = int(input("Escribe un número entero: "))

#proceso
    triangulo = calculoTriangulo(numero)

#salida
for valor in triangulo:
    print(valor)
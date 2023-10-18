#Escribir un programa que muestre por pantalla la tabla de multiplicar
#del 1 al 10.

def tablaMultiplicar():
    '''función que calcula la tabla multiplicar y da salida'''
    for numeroUno in range(1, 11):
        for numeroDos in range(1, 11):
            print(numeroUno*numeroDos,end="\t")  
    return("")
    

#entrada: no hay datos de entrada, sólo la tabla de multiplicar hasta el 10.

#proceso
multiplicación = tablaMultiplicar()

#salida
print(multiplicación)
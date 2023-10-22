#Escribir un programa que muestre por pantalla la tabla de multiplicar
#del 1 al 10.

def tablaMultiplicar():
    '''función que calcula la tabla multiplicar y da salida'''
    listas = []
    for numeroUno in range(1, 11):
        for numeroDos in range(1, 11):
            listas.append(f"{numeroUno} X {numeroDos} = {numeroUno*numeroDos}")  
    return listas


if __name__=="__main__":
#entrada: no hay datos de entrada, sólo la tabla de multiplicar hasta el 10.

#proceso
    multiplicación = tablaMultiplicar()

#salida
    for n in multiplicación:
        print(n)
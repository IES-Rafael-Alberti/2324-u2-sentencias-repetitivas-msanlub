#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

OP1 = "Este es el texto que se imprime con la opción 1"
OP2 = "Este es el texto que se imprime con la opción 2"
OP3 = "Programa finalizado"
NONE = "Error,vuelva a indicar una opción correcta."
MENU = "(1)Comenzar programa\n(2)Imprimir listado\n(3)Finalizar programa\n"

def eligeMenu(opcion:str) ->str:
    '''función que muestra la opción que elige el usuario'''
    if opcion == "1":
        return OP1
    elif opcion == "2":
        return OP2
    elif opcion == "3":
        return OP3
    else:
        return NONE

if __name__=="__main__":
    #entrada
    opcion = 0

    #procedimiento
    while opcion != "3":
        print(MENU)
        opcion= input("Indica la opción deseada: ")
        #salida
        print(eligeMenu(opcion))
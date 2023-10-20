#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

OP1 = "Este es el texto que se imprime con la opción 1"
OP2 = "Este es el texto que se imprime con la opción 2"
OP3 = "Programa finalizado"
NONE = "Error,vuelva a indicar una opción correcta."

def eligeMenu(opcion,OP1,OP2,OP3):
    '''función que muestra la opción que elige el usuario'''
    while opcion:
        if opcion == OP2:
            return OP2
        if opcion == OP1:
            return OP1
        if opcion == OP3:
            return OP3
        else:
            return NONE


if __name__=="__main__":
    #entrada
    opcion = input("(1)Comenzar programa\n(2)Imprimir listado\n(3)Finalizar programa\nIndica la opción deseada: ")
    
    #proceso
    eleccion = eligeMenu(opcion,OP1,OP2,OP3)
    
    #salida
    print(eleccion)
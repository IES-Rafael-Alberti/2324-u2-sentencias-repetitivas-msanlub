#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

FIN = "salir"

def fraseSalida(frase:str,FIN:str) -> str:
    '''función que repite la frase introducida hasta que se escriba salir'''
    return frase == FIN

if __name__=="__main__":
    #entrada
    frase = input("Escribe lo que quieras: ")

    #procedimiento
    while not fraseSalida(frase,FIN):
        #salida
        print(frase)
        #entrada
        frase = input("Escribe lo que quieras: ")
    
    print("Se acabó.")
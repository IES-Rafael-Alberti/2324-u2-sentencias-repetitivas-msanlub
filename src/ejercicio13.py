#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

FIN = "salir"

def ecoFrase(frase:str,FIN:str) -> str:
    '''función que repite la frase introducida hasta que se escriba salir'''
    while frase != FIN:
        return frase

if __name__=="__main__":
    #entrada
    frase = str(input("Escribe lo que quieras: "))

    #procedimiento
    eco = ecoFrase(frase,FIN)
    if eco == FIN:
        #salida
        print("Se acabó.")
#Escribir un programa que almacene la cadena de caracteres contraseña
#en una variable, pregunte al usuario por la contraseña hasta que
#introduzca la contraseña correcta.


CONTRASEÑA = "123456"

def contraseñaCorrecta(passw,CONTRASEÑA):
    '''función que repite hasta tener la contraseña correcta'''
    if passw != CONTRASEÑA:
        return False
    return True

if __name__=="__main__":
#entrada
    passw = input("Introduce la contraseña correcta:\n")
    
#proceso
    key = contraseñaCorrecta(passw,CONTRASEÑA)

#salida
    while not key:
        passw = input("Error.La contraseña no es correcta.Intentalo de nuevo:\n")
    print(key)
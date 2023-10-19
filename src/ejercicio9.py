#Escribir un programa que almacene la cadena de caracteres contraseña
#en una variable, pregunte al usuario por la contraseña hasta que
#introduzca la contraseña correcta.


CONTRASEÑA = "123456"

def checkPassword(passw,CONTRASEÑA):
    '''función que repite hasta tener la contraseña correcta'''
    '''if passw != CONTRASEÑA:
        return False
    return True'''
    return passw == CONTRASEÑA

if __name__=="__main__":
    passwordOk = False
    while not passwordOk: 
        #entrada
        passw = input("Introduce la contraseña correcta:\n")

        #proceso
        passwordOk = checkPassword(passw,CONTRASEÑA)
        if passwordOk is False:
            print("Contraseña incorrecta.Intentalo de nuevo.")

    #salida
    print("Contraseña correcta.")
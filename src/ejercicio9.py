#Escribir un programa que almacene la cadena de caracteres contraseña
#en una variable, pregunte al usuario por la contraseña hasta que
#introduzca la contraseña correcta.


contraseña = 123456

def contraseñaCorrecta(contraseña):
    '''función que repite hasta tener la contraseña correcta'''
    while passw != contraseña:
        passw2 = input("Contraseña incorrecta, vuelve a intentarlo: ")
    return "Contraseña correcta" 
    
#entrada
passw = input("Introduce la contraseña correcta: ")

#proceso
key = contraseñaCorrecta(contraseña)

#salida
print(key)
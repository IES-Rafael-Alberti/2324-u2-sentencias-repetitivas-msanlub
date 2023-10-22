#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetirPalabra(palabra:str) -> str:
    palabraRepetida = ""
    for i in range(10):
        palabraRepetida += palabra + "\n"
    return palabraRepetida 

if __name__=="__main__":    
#entrada
    palabra = str(input("Escribe una palabra: "))
    
#procedimiento
    bucle = repetirPalabra(palabra)

#salida
    print(bucle)
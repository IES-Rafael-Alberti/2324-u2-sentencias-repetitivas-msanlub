#Escribir un programa que pregunte al usuario su edad y muestre 
#por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def repetirEdad(edad:int) ->int:
    '''función que repite la edad de entrada de uno en uno'''
    numeros = []
    for numero in range(edad):
        numeros.append(numero+1)
    return numeros 

if __name__=="__main__":
#entrada
    edad = int(input("Escribe tu edad: "))

#procedimiento
    bucle = repetirEdad(edad)

#salida
    for valor in bucle:
        print(valor)
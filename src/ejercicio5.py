#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el
#capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 

def calculoCapital(cantidad,interes,años):
    '''funcion que calcula el capital obtenido'''
    cantidades = []
    for _ in range(años):
        cantidad *=1 + interes / 100
        cantidades.append(cantidad)
    return cantidades

if __name__=="__main__":
#entrada
    cantidad = float(input("Indica la cantidad a invertir: "))
    interes = float(input("Ahora indica el interés anual: "))
    años = int(input("Introduce el número de años: "))

#proceso
    capital = calculoCapital(cantidad,interes,años)

#salida
    contador = 1
    for valores in capital:
        print("En el año " + str(contador) + " el capital es: " + str(round(valores,2)))
        contador +=1
        
        
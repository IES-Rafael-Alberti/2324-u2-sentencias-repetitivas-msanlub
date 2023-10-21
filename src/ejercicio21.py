#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def calculoMonto(monto):
    '''función que suma la cantidad de monto'''
    cantidad = 0
    while monto > 0:
        cantidad = cantidad + monto

def calculoDescuento(monto):
    '''función que calcula el descuento si lo hay'''
    return ((monto*10) / 100)
    
if __name__=="__main__":
    #entrada
    monto = int(input("Escriba el monto de su compra: "))
    while monto < 0:
        monto = int(input("Error, escribe un número positivo: "))
    
    #proceso
    totalMonto = calculoMonto(monto)
    descuento = calculoDescuento(monto)
    #salida
    if totalMonto == 0:
        print("Fin.")
    elif totalMonto > 1000:
        print("La cantidad a pagar con descuento es: " + str(totalMonto - descuento))
    else:
        print("La cantidad a pagar es: " + str(totalMonto))
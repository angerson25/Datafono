##Problema 14 - Tuplas
#Se tiene el registro con los datos de una transacción de un cliente a partir de un datáfono en un archivo de texto como lo son: número de tarjeta, valor compra, código datáfono y fecha. Determinar el valor a cobrar por la comisión del manejo de la transacción de acuerdo a la siguiente tabla y generar las tuplas para los servicios de la transacción:
#Rango comisión
#0 - 100.000 0.5%
#100.001 - 1.000.000 0.4%
#> 1.000.000 1%

#Como respuesta se deben generar 2 tuplas, una para el establecimiento con los datos del código establecimiento (Diccionario de asignacion de datáfonos), valor comisión y neto a pagar. Otra para el banco del cliente con el número de cuenta (Diccionario de asignacion de tarjetas) y el valor de la compra.


Datafonos={1:2525,2:3535}
Tarjetas={2525:123456789,3535:987654321}


Transaccion={}

with open("transacciones.txt", "r") as f:
    x = f.readlines()
    for i in x:
        lista1=i.split(":")
        lista1[1]=lista1[1].replace("\n","")
        lista2=lista1[1].split(",")
        Transaccion.setdefault(lista1[0],lista2)
f.close()



tuplatienda=()
tuplabanco=()

for key in Transaccion:
    valorcompra=int(Transaccion[key][0])
    print(valorcompra)
    if valorcompra<=100000:
        comision=valorcompra*0.005
    elif valorcompra>100000 and valorcompra<=1000000:
        comision=valorcompra*0.004
    else:
        comision=valorcompra*0.01
    
    tuplatienda=(Datafonos[int(Transaccion[key][1])],comision,valorcompra-comision)
    
    
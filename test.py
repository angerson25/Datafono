# Diccionario de asignación de datáfonos
establecimiento_diccionario = {
    2525: "Tienda_A",
    
}

# Diccionario de tarjetas
tarjeta_diccionario = {
    2525: 126429,
}

# Diccionario de transacciones
Transacciones={}

with open("transacciones.txt", "r") as f:
    x = f.readlines()
    for i in x:
        lista1=i.split(":")
        lista1[1]=lista1[1].replace("\n","")
        lista2=lista1[1].split(",")
        Transacciones.setdefault(lista1[0],lista2)
f.close()

#calcular
for key in Transacciones:
    valor_compra = int(Transacciones[key][0])
    if valor_compra <= 100000:
        comision = valor_compra * 0.005
    elif valor_compra <= 1000000:
        comision = valor_compra * 0.004
    else:
        comision = valor_compra * 0.01

    #neto a pagar
    neto_a_pagar = valor_compra - comision

    # Generar tupla para el establecimiento
    codigoestablecimiento=int(Transacciones[key][1])
    
    tupla_establecimiento = (codigoestablecimiento, comision, neto_a_pagar)

    # Generar tupla para el banco del cliente
    numerocuenta=int(tarjeta_diccionario[codigoestablecimiento])
    tupla_banco_cliente = (numerocuenta, valor_compra
    )

    # Imprimir resultados
    print(f"Tupla para el establecimiento:", tupla_establecimiento)
    print(f"Tupla para el banco del cliente: ", tupla_banco_cliente)
    print("--------")

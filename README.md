# Ejercicio datafono

## #Se tiene el registro con los datos de una transacción de un cliente a partir de un datáfono en un archivo de texto como lo son: número de tarjeta, valor compra, código datáfono y fecha. Determinar el valor a cobrar por la comisión del manejo de la transacción de acuerdo a la siguiente tabla y generar las tuplas para los servicios de la transacción:

## Rango comisión
## 0 - 100.000 0.5%
## 100.001 - 1.000.000 0.4%
## > 1.000.000 1%

## Como respuesta se deben generar 2 tuplas, una para el establecimiento con los datos del código establecimiento (Diccionario de asignacion de datáfonos), valor comisión y neto a pagar. Otra para el banco del cliente con el número de cuenta (Diccionario de asignacion de tarjetas) y el valor de la compra.
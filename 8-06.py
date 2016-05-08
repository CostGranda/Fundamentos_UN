# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:20:00 2016

@author: coste
"""
"""
Cree un subrograma en Python 3.4 llamado identidad.py, 
con una función llamada iden que genera una matriz identidad. 
La función recibe como argumento un número entero que corresponde al tamaño de una matriz cuadrada
 y retorna como resultado la matriz identidad del tamaño ingresado.

Además, cree un programa en Python 3.4 denominado main.py
 que le solicite al usuario un número entero, y luego lo utilice como argumento de la función 
 en el subprograma, y finalmente muestre la matriz identidad (cada fila en una linea diferente). 
 Muestre exclusivamente lo solicitado anteriormente sin enunciados extra que lo acompañen.

Puede consultar información de referencia sobre la matriz identidad en: 
https://es.wikipedia.org/wiki/Matriz_identidad

Nota: En VPL de Moodle debe estar primero el archivo del programa y luego el del subprograma.

Por ejemplo, si el usuario ingresa el número 3, el programa debe mostrar:

[1, 0, 0]
[0, 1, 0]
[0, 0, 1]
"""

num = 3

def iden(num):
    matriz = [[0 for i in range(num)] for j in range(num)]

    for i in range(num):
        for j in range(num):
            if(i==j):
                matriz[i][j] = 1
    return matriz

#matriz = iden(num)
for fila in iden(num):
    print(fila)
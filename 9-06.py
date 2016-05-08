# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:29:27 2016

@author: coste
"""

matriz = eval(input())
lista = []

for i in range(len(matriz)):
    if (matriz[i][1] > 300000):
        matriz[i][1] = matriz[i][1] - (matriz[i][1] * 0.2)
    elif (matriz[i][1] < 100000):
        matriz[i][1] = matriz[i][1] - (matriz[i][1] * 0.05)
    else:
        matriz[i][1] = matriz[i][1] - (matriz[i][1] * 0.1)
    lista.append(round((matriz[i][1] - matriz[i][0]), 2))

print(lista)
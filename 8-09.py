# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:44:50 2016

@author: coste
"""

def esc(matriz, num):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = matriz[i][j] * num
    return matriz

num = 19
matriz = [[3, 8, 3], [9, 5, 3], [5, 2, 8]]
for fila in esc(matriz, num):
    print(fila)
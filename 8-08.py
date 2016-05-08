# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:39:32 2016

@author: coste
"""

def det(matriz):
    det = 1
    for i in range(len(matriz)):
        det *= matriz[i][i]
    return det

matriz = [[88, 27, 46], [0, 57, 20], [0, 0, 15]]
print(det(matriz))
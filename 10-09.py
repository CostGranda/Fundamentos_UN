# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:39:13 2016

@author: coste
"""

matriz = [[1, 12], [2, 8]]
acu=0
for i in range(len(matriz)):
    acu += matriz[i][1]
print(acu/len(matriz))
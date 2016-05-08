# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:33:20 2016

@author: coste
"""

matriz = eval(input())

multas = []
for i in range(len(matriz)):
    if ((matriz[i][1] / matriz[i][0]) > 3):
        multas.append(100000)
    else:
        multas.append(0)

print(multas)
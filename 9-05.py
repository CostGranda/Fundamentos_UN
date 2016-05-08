# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:35:53 2016

@author: coste
"""

lista = eval(input())

for i in range(len(lista)):
    if (lista[i] > 300000):
        lista[i] -= lista[i] * 0.40
    elif (lista[i] < 100000):
        lista[i] -= lista[i] * 0.05
    else:
        lista[i] -= lista[i] * 0.2

print(lista)
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:46:18 2016

@author: coste
"""

def dif(lista):
    areas = []
    for elemento in lista:
        areas.append((elemento**2) * 3.14)
    return max(areas) - min(areas)

lista = [71, 35, 57, 32]
print(dif(lista))
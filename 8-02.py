# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:40:42 2016

@author: coste
"""

def sumar(x, y):
    suma = 0
    resta = 0
    for i in range(x, y+1):
        if (i%2 == 0):
            suma += i
        else:
            resta -= i
    return suma, resta

x = int(input())
y = int(input())

print(sumar(x,y))        
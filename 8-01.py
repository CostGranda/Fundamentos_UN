# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:39:03 2016

@author: coste
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input())
print(factorial(numero))
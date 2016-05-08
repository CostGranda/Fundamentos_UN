# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:15:44 2016

@author: coste
"""

def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(a, a % b)
a = 8
b = 10
print(mcd(a,b))
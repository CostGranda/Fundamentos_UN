# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:32:21 2016

@author: coste
"""

palabra = input()
if(palabra == palabra[::-1]):
    print(palabra)
else:
    print("error")
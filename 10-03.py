# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:11:11 2016

@author: coste
"""

lista = eval(input())
numero = int(input())
sum=0
for elemento in lista[:numero]:
    sum += elemento
print(sum)
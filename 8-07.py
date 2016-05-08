# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:29:02 2016

@author: coste
"""

def sumar(m1, m2):
    m3 = [[0 for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3

m1 = [[14, 6], 
      [46, 43]]
      
m2 = [[24, 67], 
      [33, 13]]
      
print(sumar(m1, m2))
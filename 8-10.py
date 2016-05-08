# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:49:58 2016

@author: coste
"""

def prod(m1, m2):
    m3 = [[0 for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):            
                m3[i][j] += m1[i][k] * m2[k][j]
            
    return m3

m1 = [[0, 6], [6, 6]]
m2 = [[3, 4], [8, 1]]

for fila in prod(m1, m2):
    print(fila)
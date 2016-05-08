# -*- coding: utf-8 -*-
"""
Created on Sat May  7 20:32:45 2016

@author: coste
"""

matriz = [[10, 12], [3, 6]]
areas =[]
for i in range(len(matriz)):
     areas.append((matriz[i][0] * matriz[i][1])/2)
print(areas)
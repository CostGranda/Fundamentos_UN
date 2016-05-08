# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:58:02 2016

@author: coste
"""

def esprimo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

lista =  [56, 71, 82, 15, 61, 68]
otralista = []
con = 1
for elemento in lista:
    if (esprimo(elemento)):
        otralista.append(elemento)
    else:
         i = 1
         while(True):
             if(esprimo(elemento+i)):
                 otralista.append(elemento+i)
                 break
             i+=1

print(otralista)
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:27:52 2016

@author: coste
"""

def conversor(moneda, cantidad):
    euros = 0.00029
    dolares = 0.00033
    yenes = 0.0368
    reales = 0.0012
    if(moneda == 'dolar'):
        return str(round((dolares * cantidad),2)) + " USD"
    elif (moneda == 'euro'):
        return str(round((euros * cantidad),2)) + " EUR"
    elif (moneda == 'yen'):
        return str(round((yenes * cantidad),2)) + " JPY"
    elif (moneda == 'real'):
        return str(round((reales * cantidad),2)) + " BRL"

print(conversor("real", 26912546 ))
        
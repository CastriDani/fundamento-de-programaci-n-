# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:58:01 2021

@author: santi
"""

def num_menor():
    n1 = int(input('Ingrese un número: '))
    n2 = int(input('Ingrese un número: '))
    n3 = int(input('Ingrese un número: '))
    if n1 < n2 and n1 < n3:
        print(n1)
    else:
        if n2 < n3:
            print(n2)
        else:
            print(n3)
num_menor()
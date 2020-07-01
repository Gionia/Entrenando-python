#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:24:53 2020
ProgramName:Encontrar el mini y maximo en un listado
@author: giovannyencinia
"""
from random import sample
def minimo(lista):#i dice desde que elemento se empezara a encontrar el valñor minimo
    j=0
    i=0
    while i<len(lista)-1:
        if lista[j]<lista[i+1]:    
            menor=lista[j]
        else:
            menor=lista[i+1]
            j=i+1
        i+=1
    return menor

def maximo(lista):
    i=0
    j=0
    while i<len(lista)-1:
        if lista[j]>lista[i+1]:
            mayor=lista[j]
        else:
            mayor=lista[i+1]
            j=i+1
        i+=1
    return mayor
lista=sample(range(100),10)
print(lista)
menor=minimo(lista,7)
print(menor)
       

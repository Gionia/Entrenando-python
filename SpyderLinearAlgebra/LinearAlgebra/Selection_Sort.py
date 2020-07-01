#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:00:45 2020
Program_Name: Selection_Sort
@author: giovannyencinia
"""


def select_sort(lista): 
    i=0
    while i<len(lista): #se ejecuta segun el tamaño del arreglo
        j=i+1  #Se  tiene una sucesion de numeros se 3,1,2,3,1,5, j es el termino con ind 1 al iniciar
        mini=i #mini es el termino 0 al iniciar
        while j<len(lista):
            if lista[mini]>lista[j]: #si el elemento en 0 es mayor a el elemento en  1 entonces decimos
                mini=j                 #que el minimo debe ser el elemento del ind 1
            j+=1                        #asi se encuentra el elemento menor
        ward=lista[i]                       
        lista[i]=lista[mini]
        lista[mini]=ward
        i+=1
    return lista


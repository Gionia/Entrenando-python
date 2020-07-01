#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:21:00 2020
Name program:Bubble sorting
@author: giovannyencinia
"""
#Bubble sort es un metodo de ordenamiento con O(n²), es el peor algoritmo de ordenamiento
def bsort(list):
    list=[2,1,4,5,6,7,55]
    a=len(list)
    j=1
    while j <a:
       i=0
       while i<a-1:
            if list[i]>list[i+1]:
                ward=list[i]
                list[i]=list[i+1]
                list[i+1]=ward
            i+=1
       a-=1
       
    print(list)
    return

def bsorti(list):#Método bubble sort ordenado de mayor a menor
    a=len(list)
    j=1
    while j <a:
       i=0
       while i<a-1:
            if list[i]<list[i+1]:
                ward=list[i]
                list[i]=list[i+1]
                list[i+1]=ward
            i+=1
       a-=1
       
    print(list)
    return
    

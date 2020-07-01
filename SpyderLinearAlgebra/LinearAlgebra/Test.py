#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:42:57 2020

@author: giovannyencinia
"""
import sympy as sp
import numpy as np
from random import sample
import BubbleSorting as bs
import Toolg as MM

x=sp.Symbol('x', real=True)
a=sp.E**(sp.I*x)
b=a.expand(complex=True)
c=(a**3).expand(complex=True).expand(trig=True)

ma=np.matrix([[1.,2,3],[2.0,3.5,6],[1.,2,3]])

'''np.random.radint(numero de elementos,size=(m,n))'''#funciona como declarar matrix
w=np.random.randint(9,size=(1,9))
w1=w.T
kiko=[1,2,3,4]




list=range(100)
list=sample(list,15)
print(list)

maximito=MM.maximo(list)
print(maximito)
print(MM.minimo(list))


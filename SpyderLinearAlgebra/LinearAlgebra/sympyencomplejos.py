#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:42:57 2020

@author: giovannyencinia
"""
import sympy as sp
'Siempre debemos especificar si nuestra variables es real o compleja, de lo contrario los resultados peuden variara  los esperados'
x=sp.Symbol('x',real=True)#True siempre es en mayusculas
a=sp.E**(sp.I*x)
b=a.expand(complex=True)
c=(a**3).expand(complex=True).expand(trig=True)#los expands se realizan secuencialmente, 
'primero se hace a**3 esta se expande y se muestra un cos(3x)+.. y usando exp trig encuentra una formula y desarrolla'
y=sp.Symbol('y')#Symbol siempre en mayusculas
f=sp.solve(y**4-sp.I,y)
for i in f:
   print( i.evalf())



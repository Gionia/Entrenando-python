#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:59:29 2020

@author: giovannyencinia
"""

import matplotlib.pyplot as mp
import numpy as np


''' cada lista contiene elementos correspondientes a abcisas y ordenadas respectivamente con 
correspiondecia uno a uno es decir para la primera lista el elementodel indice 0 le corresponde una ordenada de la segunda
lista cuyo indice del elemento tambien es el cero'''
f= lambda x: np.sin(x)
x=np.linspace(9,8)
mp.plot(x,f(x),"s") 
mp.ylabel("eje y")
mp.xlabel("eje x")
mp.show()

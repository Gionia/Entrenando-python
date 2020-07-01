#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:36:28 2020

@author: giovannyencinia
"""

from random import sample

def bsort(list):
    a=len(list)
    i=0
    print(list)
    while i<a-1:
       
       if list[i]>list[i+1]:
          ward=list[i]
          list[i]=list[i+1]
          list[i+1]=ward
       print(list)
       print(i)
       i+=1
           
      
        
   
    
     
             
       
    return
    
list=range(100)
list=sample(list,8)
list=[8,3,25,1,9,35,0]
bsort(list)

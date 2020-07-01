#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
def first_view(df):
    """This function gives the shape of the DataFrame and the sum of the NA values
        across the columns"""
    sep = "/-/-/-/-/-/-/-//-/-/-/-/-/-/-/-//-/-/-/-/-/-/-//-/-/-/-/-/-/-/\n"
    print(f"The size of DataFrame is:{df.shape}\n")
    print(f"{sep}")
    print(f" The total of NA per column is: \n\n{df.isnull().sum()} \n")
    print(f"{sep}")
    print("***************The value_counts per column*****************\n")
    for columns in df.columns:
        print(f"{sep}")
        print(f"{df[columns].value_counts()}\n")
            
    #end function first view

def dummies(df, columns, pref = 'dumn'):
    """ This function uses the method get_dummies and concatennates the result 
        on the DataFrame """
    dummies = pd.get_dummies(df[columns], prefix = pref)
    del(df[columns])
    df = pd.concat([df, dummies], axis = 1)
    
    

        
    
    
    


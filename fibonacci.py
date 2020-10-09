# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:27:30 2020

@author: AKASH
"""
i=int(input("Enter the number: "))
n=0
a=-1
b=1
while i>n:
    fibonacci=a+b
    a=b
    b=fibonacci
    n+=1
    print(fibonacci)
    
    
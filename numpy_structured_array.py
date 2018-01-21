# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:09:31 2018

@author: Sanidhya
"""

import numpy as np

name = ['Sanidhya','Alice','Bob','Cathy']
age=[19,25,23,18]
weight = [59.5,61.0,84.5,52.2]

#using coumpund datatype for structured array 
data = np.zeros(4,dtype={'names':('name','age','weight'),'formats':('U10','i4','f8')})
print(data.dtype)
#populating data in data array
data['name']=name
data['age']=age
data['weight']=weight
print(data)

print(data[2:]) #slicing data after index 2
print(data[np.less(data['age'],20)]['name']) #printing name of people of age < 20

#more advanced compound types 

tp = np.dtype([('id','i8'),('mat','f8',(3,3))])
X = np.zeros(1,dtype=tp)
print(X) #print a complete array
print(X['mat'][0]) #print an array with zero index and of mat property

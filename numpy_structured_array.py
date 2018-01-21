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
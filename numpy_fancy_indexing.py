# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 00:04:08 2018

@author: Sanidhya
"""

import numpy as np

x = np.random.RandomState(42).randint(100,size = 10)
ind = [3,4,7]
print(x[ind])

ind = np.array([[3,6],[4,5]])
print(x[ind])

X = np.arange(12).reshape(3,4) #matrix of 3x4 0-12
print(X)
row = np.arange(3)
col = np.array([2,1,3])
print(X[row,col])
print(X[row[:,np.newaxis],col])
print(row[:,np.newaxis]*col)

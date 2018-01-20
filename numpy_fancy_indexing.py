# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 00:04:08 2018

@author: Sanidhya
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

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

print(X[2,[2,0,1]])
print(X[1:,[2,0,1]]) #used slicing to index array 
mask = np.array([1,0,1,0],dtype=bool)
print(X[row[:,np.newaxis],mask])

mean=[0,0]
cov = [[1,2],[2,5]]
X = np.random.RandomState(42).multivariate_normal(mean,cov,100)
print(X)
plt.scatter(X[:, 0], X[:, 1])
indices = np.random.choice(X.shape[0],20,replace=False)
indices
selection = X[indices] #fancy indexing 
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],s=200);

x = np.zeros(10)
i = np.array([2,3,3,4,4,4])
np.add.at(x,i,1)
print(x)
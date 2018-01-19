# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:31:49 2018

@author: Sanidhya
"""
import numpy as np

a=np.array([1,2,3])

a+5 #adding an scalar to a 

M = np.ones((3,3))
M+a-1 #addition of array  a and subraction of scalar 1

a=np.arange(3)
b=np.arange(3)[:,np.newaxis] #creating a coloumn array 
print(a)
print(b)
print(a+b) #streching both the 1D arrays into 2D

M = np.ones((2,3))
a= np.arange(3)
M+a

X = np.random.random((10,3))
Xmean = np.mean(X,axis=0)
Xmean
X_centered = X-Xmean
X_centered
X_centered = X_centered.mean(0)
X_centered

#Plotting a 2D function

x = np.linspace(0,5)
y = np.linspace(0,5)[:,np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

import matplotlib.pyplot as plt

plt.imshow(z,origin='lower',extent=[0,5,0,5],cmap='viridis')
plt.colorbar();
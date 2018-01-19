# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:06:34 2018

@author: Sanidhya
"""

import numpy as np

#generate a single dimesion array
x1 = np.random.randint(10,size=6)

#generate a two dimension array 
x2 = np.random.randint(10,size=(3,4))

#genareate a 3 dim array 
x3  = np.random.randint(10,size=(3,4,5))

#some basic functions on numpyarray 
print("x3 ndim",x3.ndim)
print("x3 shape",x3.shape)
print("x3 size",x3.size)

#some basic slicing methods for array 
x= np.arange(10)

print(x[:5])   #first five elements 
print(x[5:])   #elements after index 5
print(x[4:7])  #subarray from index 4-7
print(x[::2])  #every element with index diff of 2
print(x[1::2]) #every element with index diff of 2 starting from 1
print(x[::-1]) #elements reversed form 
print(x[5::-2])#every other element in a reversed from index 5

#excessing sub arrays of multi dim array 
print(x2[2]) #print a sub array
sub_array =x2[:2,:2] #extracting a 2*2 array from x2
x2_sub_copy = x2[:2,:2].copy()

#reshaping array
grid  = np.arange(1,10).reshape((3,3))
print(grid)

#reshaping into colounm matrix 
x= np.arange(1,10)
x_reshape = x.reshape((9,1)) 
print(x_reshape)
x_newaxis = x[:,np.newaxis] #conversion using newaxis function 
print(x_newaxis)

x=[1,34,5]
y=[5,5,6]
x_y = np.concatenate([x,y])
z=[1,4,5]
z_con = np.concatenate([x_y,z])
print(z_con)

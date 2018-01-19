# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:03:47 2018

@author: Sanidhya
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns; sns.set();

L = np.random.random(100)
print(sum(L))

big_array = np.random.rand(1000000)
print(min(big_array),max(big_array)) #to calculate min and max 

#using numpy packages 
print(big_array.sum(),big_array.min(),big_array.max())

#operations on multidimensional arrays 
M = np.random.random((3,4))
print(M)
M.sum() #to calculate a sum of M 
#M.max(axis=0)
print(M.max(axis=0)) # to calculate the max from axis 0 i.e. coloumn
print(M.max(axis=1)) # to calculate max from axis 1 i.e. rows

"""All the stats operations on array can be performed using various operations in the 
   library such as mean,mod,median and others and can also be called as a NaN-Safe version"""
data  = pd.read_csv('data/president_height.csv') #heights imported in a data variable 
heights = np.array(data['height(cm)']) #heights stored as an numpyarray

#printing some basic results such as median, mode,mean,min,max and percentile 
print("Mean Height:",np.mean(heights))
print("Std of Heights:",np.std(heights))
print("Variance of Heights",np.var(heights))
print("Min height",heights.min())
print("Max Heights",heights.max())
print("25th Percentile",np.percentile(heights,25))
print("75th percentile",np.percentile(heights,75))

plt.hist(heights)
plt.title("Height Distribution of US President")
plt.xlabel('height(cm)')
plt.ylabel('numbers')
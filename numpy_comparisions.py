# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:15:33 2018

@author: Sanidhya
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn; seaborn.set() 

rainfall  = pd.read_csv('data/Seattle2014.csv')
inches = rainfall['PRCP'].values/254.0

plt.hist(inches,40)

#Some boolean expression
x = np.arange(1,6)
print(np.less(x,3)) #compare array elements with scalar
print(np.greater(x,3)) #greater with an scalar elements 
print(np.less_equal(x,3)) #<= with an scalar 
print(np.greater_equal(x,3)) #>= with scalar
print(np.equal(x,3)) #== with a scalar 
print(np.not_equal(2*x,x**2)) #!= with a scalar 

x  = np.random.RandomState(0).randint(10,size=(3,4)) # generate a 2D array for a random state 0 in x 

print(np.count_nonzero(x<6)) #check all now zeros for condition
print(np.sum(x < 6)) # print count of all the elements is a matrix satisfying condition
print(np.sum(x < 6, axis=1)) # on axis 1
print(np.sum(x > 6, axis=0)) # on axis 0
print(np.any(x < 6)) # check if any of elements in matrix follow condition
print(np.all(x < 6)) #check if all the elements in matrix follows the condition 

#using some boolean opperators 
print(np.sum(np.bitwise_and(inches > 0.5, inches < 1))) 
print(np.sum(~((inches <= 0.5) | (inches >=1))))
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:14:12 2018

@author: Sanidhya
"""

import numpy as np
import scipy.special as spl

x=[1,3,5]
print("gama(x)",spl.gamma(x))
print("ln|gama(x)",spl.gammaln(x))
print("beta",spl.beta(x,2))

#some error functions 
x = np.array([0, 0.3, 0.7, 1.0])
print("erf",spl.erf(x))
print("erfc",spl.erfc(x))
print("erfinv",spl.erfcinv(x))

#Advanced functions

x=np.arange(5)
y=np.empty(5)
np.multiply(x,10,out=y) #use output function to specify output at specicific location 
print(y)

y=np.zeros(10)
np.power(2,x,out=y[::2])
#np.power(x,1,out=y[1::2])
print(y)

#Some advanced calculation
x=np.arange(1,6)
print(np.add.reduce(x)) #reduce into single output 
print(np.multiply.reduce(x))
#showing intermediate output of every step
print(np.add.accumulate(x))
print(np.multiply.accumulate(x))
print(np.multiply.outer(x,[1,10,20,30,40]))#show all possible outputs 
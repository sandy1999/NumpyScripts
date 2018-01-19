p# -*- coding: utf-8 -*-

import numpy as np
x=np.arange(5)

#exploring some universal functions of numpy 

print("x=",x)
print("x+5",x+5)
print("x-5",x-5)
print("x*2",x*2)
print("x/2",x/2)
print("x//2",x//2) #floor operation

#unary functions
print("-x",-x)
print("x**2",x**2)
print("x%2",x%2)

print(-(0.5*x+1)**2) #some random expression for tuple

#some equivalent functions using np
print(np.add(x,2))#x+2
print(np.subtract(x,5))#x-5
print(np.negative(x))#-x
print(np.multiply(x,2))#x*2
print(np.floor_divide(x,2))#x//2
print(np.mod(x,2))#x%2
print(np.divide(x,2))#x/2
print(np.power(x,2)) #x**2

#some more functions 
x=np.array([-2,-1,-3,4,5])
print(np.abs(x))

#trignometric functions 
theta  = np.linspace(0,np.pi,3)
print("theta",theta)
print("sin(theta)",np.sin(theta))
print("cos(theta)",np.cos(theta))
print("tan(theta)",np.tan(theta))
#inverse trignometric functions 
theta=[-1,0,1]
print("arcsin(theta)",np.arcsin(theta))
print("arccos(theta)",np.arccos(theta))
print("arctan(theta)",np.arctan(theta))

#lograthmic function and exponential functions
x=[1,2,3]
print("e^x",np.exp(x))
print("2^x",np.exp2(x))
print("3^x",np.power(3,x))

x=[1,2,4,10]
print("ln(x)",np.log(x))#log base 'e'
print("log2",np.log2(x))#log base '2'
print("log10(x)",np.log10(x))#log base '10'
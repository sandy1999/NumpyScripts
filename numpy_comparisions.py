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
inches = rainfall['PRCP'].values

plt.hist(inches,40)
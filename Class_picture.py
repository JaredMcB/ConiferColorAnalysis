# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:05:01 2020

@author: jared
"""


import matplotlib.pyplot as ppt
import numpy as np

fig, ax = ppt.subplots()

color_class = list(dict_of_HCV_Classes[1])

n = 0
for color in color_class:
    n += 1
    y = np.floor(n/10)
    x = n % 10
    color = tuple([a/255 for a in color])
    ax.scatter(x, y, c=color, s=150) 
    print(color)
    
ppt.show()



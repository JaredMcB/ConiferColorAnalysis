# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:27:07 2020

@author: jared
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
import random



with open('Munsell_RGB_lookuptable.data', 'rb') as MRlt:
    Munsell_RGB_lookuptable = pickle.load(MRlt)

L = len(Munsell_RGB_lookuptable[0])

Munsell_list, RGB_list = Munsell_RGB_lookuptable

## get Colors_of_leaves and here will be the index

#Colors_of_leaves_ind = [Munsell_list.index(color) for color in Colors_of_leaves]

Colors_of_leaves_ind = random.sample(range(L),300)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs, ys, zs = [], [], []
for rbg in [RGB_list[i] for i in Colors_of_leaves_ind]:
    xs.append(rbg[0])
    ys.append(rbg[1])
    zs.append(rbg[2])
ax.scatter(xs,ys,zs, c='r', marker='o',s=4)

xs, ys, zs = [], [], []
other_colors_ind = list(set(range(L)) - set(Colors_of_leaves_ind))
for rbg in [RGB_list[i] for i in other_colors_ind]:
    xs.append(rbg[0])
    ys.append(rbg[1])
    zs.append(rbg[2])
ax.scatter(xs,ys,zs, c='b', marker='o',s=4)

ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')

plt.show()
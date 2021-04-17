# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:52:59 2020

@author: jared
"""


import matplotlib.pyplot as ppt

rgb_list_fromfun = [my_HVC2RGB(Munsell) for Munsell in Munsell_list]


nonerror_ind_bol = [tuple(rgb) != tuple([96,83,79]) for rgb in rgb_list_fromfun]

L = len(nonerror_ind_bol)

nonerror_ind = []
for i in range(L):
    if nonerror_ind_bol[i]:
        nonerror_ind.append(i)
        
start = nonerror_ind[0]
stop = nonerror_ind[-1]
K = range(start,(stop + 1))

differ = [tuple(rgb_list_fromfun[i]) == tuple(rgb_list_fromtable[i]) for i in K]

LIST = random.sample(K,10)

[tuple(rgb_list_fromfun[i] + rgb_list_fromtable[i]) for i in LIST]

[Munsell_list[i] for i in LIST]

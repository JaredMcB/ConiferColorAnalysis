# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import colour
import numpy as np
import math
import urllib.request
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import pickle

# The *Munsell Renotation System* colour we would like to convert
# to *sRGB* colourspace.
data_url = 'http://www.rit-mcsl.org/MunsellRenotation/all.dat'
data_file = 'all.dat'

def fetch(url = data_url, fname = data_file, clobber = False):
    # If we're not clobbering the file, quit early if we can read it.
    if not clobber:
        try:
            with open(fname) as f:
                return
        except FileNotFoundError:
            pass
    # Fetch the data from the internet.
    data = urllib.request.urlopen(url)
    with open(fname, 'w') as f:
        f.write(data.read().decode())

def load(fname = data_file):
    with open(fname) as f:
        return [line for line in f]

C = colour.ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['C']
def my_HVC2RGB(HVC):
    xyY = colour.munsell_colour_to_xyY(HVC)
    XYZ = colour.xyY_to_XYZ(xyY)
    # The last step will involve using the *Munsell Renotation System*
    # illuminant which is *CIE Illuminant C*:
    # http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/colorimetry/illuminants.ipynb#CIE-Illuminant-C
    # It is necessary in order to ensure white stays white when
    # converting to *sRGB* colourspace and its different whitepoint 
    # (*CIE Standard Illuminant D65*) by performing chromatic 
    # adaptation between the two different illuminant.
    rgb = colour.XYZ_to_sRGB(XYZ, C)
    RGB = [np.uint8(round(255*x)) for x in rgb]
    return RGB

data = load()
Munsell_list = [datum.split()[0] + ' ' 
                + datum.split()[1] +'/'
                +datum.split()[2] for datum in data[1:]]

xyY_list_fromtable = [[np.float(x) for x in datum.split()[3:]
                       ] for datum in data[1:]]

# adjust for y=0's
for xyY in xyY_list_fromtable:
    if xyY[1] == 0:
        xyY[1] = 1e-50


# Thuis didn't work
#xyY_list = [colour.munsell_colour_to_xyY(HVC) for HVC in Munsell_list]


XYZ_list_fromtable = [colour.xyY_to_XYZ(xyY) for xyY in xyY_list_fromtable]

rgb_list_fromtable = [[np.uint8(round(255*x)) for x in colour.XYZ_to_sRGB(XYZ, C)
                       ] for XYZ in XYZ_list_fromtable]
L = len(rgb_list_fromtable)
Munsell_RGB_lookuptable = [[Munsell_list[i],rgb_list_fromtable[i]] for i in range(L) ]

with open('Munsell_RGB_lookuptable.data', 'wb') as MRlt:
    # store the data as binary data stream
    pickle.dump(Munsell_RGB_lookuptable, MRlt)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs, ys, zs = [], [], []
for rbg in rgb_list_fromtable:
    xs.append(rbg[0])
    ys.append(rbg[1])
    zs.append(rbg[2])

ax.scatter(xs,ys,zs, c='r', marker='o',s=4)

ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')

L = len()
Colors_of_leaves_ind = random.sample(range(L))
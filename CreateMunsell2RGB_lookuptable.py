# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import colour
import numpy as np
import urllib.request
import pickle
import random


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
    try:
        xyY = colour.munsell_colour_to_xyY(HVC)
    except AssertionError:
        xyY = [0,1,1]
        
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
Munsell_list = []
xyY_list_fromtable = []

for datum in data[1:]:
    Munsell_list.append(datum.split()[0] + ' ' 
                        + datum.split()[1] +'/'
                        +datum.split()[2])
    xyY = [np.float(x) for x in datum.split()[3:]]
    xyY[2] /= 100
    xyY_list_fromtable.append(xyY)

                               
# adjust for y=0's
for xyY in xyY_list_fromtable:
    if xyY[1] == 0:
        xyY[1] = 1e-50

XYZ_list_fromtable = [colour.xyY_to_XYZ(xyY) for xyY in xyY_list_fromtable]

rgb_list_fromtable = [[np.uint8(round(255*x)) for x in colour.XYZ_to_sRGB(XYZ, C)
                       ] for XYZ in XYZ_list_fromtable]

rgb_list_fromfun = [my_HVC2RGB(Munsell) for Munsell in Munsell_list]

nonerror_ind_bol = [tuple(rgb) != tuple([96,83,79]) for rgb in rgb_list_fromfun]

L = len(nonerror_ind_bol)

nonerror_ind = []
for i in range(L):
    if nonerror_ind_bol[i]:
        nonerror_ind.append(i)
        
start = nonerror_ind[0]
stop = nonerror_ind[-1]

# Truncate to include only non errored colors
Munsell_RGB_lookuptable = [Munsell_list[start:(stop+1)],
                           rgb_list_fromtable[start:(stop+1)]]

# Pickle Look up table
with open('Munsell_RGB_lookuptable.data', 'wb') as MRlt:
    # store the data as binary data stream
    pickle.dump(Munsell_RGB_lookuptable, MRlt)


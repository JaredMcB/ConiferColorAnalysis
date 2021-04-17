# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:41:51 2020

@author: jared
"""


import pickle
from sklearn.neighbors import KNeighborsClassifier
import csv
import numpy as np


### Import Munsell to RGB lookup table by pickle
with open('Munsell_RGB_lookuptable.data', 'rb') as MRlt:
    Munsell_RGB_lookuptable = pickle.load(MRlt)

L = len(Munsell_RGB_lookuptable[0])
Munsell_list, RGB_list = Munsell_RGB_lookuptable

### Import list of munsell colors of interest
RGB_of_interest = []
with open('colors_of_interest_RGB.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        RGB = [np.int(st) for st in row[:3]]
        RGB_of_interest.append(RGB)

L_int = len(RGB_of_interest)

classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(RGB_list, Munsell_list)

Munsell_of_interest = classifier.predict(RGB_of_interest)


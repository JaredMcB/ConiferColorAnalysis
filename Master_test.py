# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:14:53 2020

@author: jared
"""
import pickle
from sklearn.neighbors import KNeighborsClassifier
import csv
from PIL import Image
import numpy as np
import os

### Import Munsell to RGB lookup table by pickle
with open('Munsell_RGB_lookuptable.data', 'rb') as MRlt:
    Munsell_RGB_lookuptable = pickle.load(MRlt)

L = len(Munsell_RGB_lookuptable[0])
Munsell_list, RGB_list = Munsell_RGB_lookuptable


### Import list of munsell colors of interest
Colors_of_interest = []
with open('colors_of_interest_test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        Colors_of_interest.append(row[0])
L_int = len(Colors_of_interest)  


### Get indices corresponding to colors of interest
Colors_of_interest_ind = [Munsell_list.index(color) for color in Colors_of_interest]
other_colors_ind = list(set(range(L)) - set(Colors_of_interest_ind))      

### Get RGB's of interest
RGB_of_interest = [RGB_list[i] for i in Colors_of_interest_ind]

### Creat dictionary of HVC classes
dict_of_HCV_Classes = {}
for i in range(L_int):
    dict_of_HCV_Classes[i] = set([tuple(RGB_of_interest[i])])
dict_of_HCV_Classes[L_int] = set([tuple(RGB_list[i]) for i in other_colors_ind])
    
classifier = KNeighborsClassifier(n_neighbors=1)
y_train = list(range(L_int)) + [L_int]*(L - L_int)
X_train = [rgb for rgb in RGB_of_interest
            ] + [RGB_list[i] for i in other_colors_ind]
classifier.fit(X_train, y_train)

###
os.system('clr')

orignial_directory = os.getcwd()
desired_directory = 'C:\\Users\\jared\\Desktop\\Picture Directory'
os.chdir(desired_directory)

folders = os.listdir('.')

for folder in folders:
    csv_rows = []
    
  
    # Push into the folder in for loop
    os.chdir('.\\' + folder)
    print('processing images in ' + folder)
    
    # get list of file (image) names in current folder
    files = os.listdir('.')
    
    for file in files:
        # mount image for extraction
        im = Image.open(file)
        size = im.size
        
        # # Crop COde
        # crop_box = (220,60,747,520)
        # crop_size = (crop_box[2] - crop_box[0])*(crop_box[3] - crop_box[1])
        # im = im.crop(crop_box)
        # image_colors = im.getcolors(crop_size)
        
        image_colors = im.getcolors(size[0]*size[1])
        
        #Build row name. This is a string that will appear at the left most colum of the csv. One 
        # row per image.
        row_name = folder + '_' + file.split('.')[0]
        
        # start to build the row that will be written. 
        csv_row = [row_name]
        row_counts = np.zeros(L_int+1)
        # Here we loop over the colors
        for color in image_colors:
            # Classify color first with dictionary then knn
            for i in range(0,L_int+1):
                if tuple(color[1]) in dict_of_HCV_Classes[i]:
                    row_counts[i] += color[0]
                    break
            else:
                i = np.int(classifier.predict([color[1]])[0])
                row_counts[i-1] += color[0]
                dict_of_HCV_Classes[i].add(tuple(color[1]))
        
        # Write the row info to the csv_file
        csv_rows.append(csv_row+list(row_counts))
        
    os.chdir(orignial_directory)
    with open('color_data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_rows)
    os.chdir(desired_directory)
    # We continue this way till we
        

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



from PIL import Image
import numpy as np

import os
import csv

# include Lists
# 1. crop control
# Based on the where the picture is from (which is identified by file name) we can crop the image in a safe way
# this lists is a list of tuples. First is a string that identifies the string we look for to identify the pictures 
# type. Second is the crop specifications. it is a box a 4-tuple (left, upper, right, lower)
# example:
crop_control = [('est',(10,18,80,52))]

#
# 2. Colors we are interested in these will be the column headers. Its form should be as a lists of 3-tuple (r,g,b) 
# the list is called target_colors.
# example:
target_colors = [(32,172,67),(255,255,255),(237,28,34),(255,229,233),(32,178,80)]


os.system('clr')

orignial_directory = os.getcwd()
desired_directory = 'C:\\Users\\McBride Family\\Pictures\\Test_directory'
os.chdir(desired_directory)

folders = os.listdir('.')





for folder in folders:
    csv_rows = []
    # Check if crop control string is in folder name
    for cc in crop_control:
        if cc[0] in folder: 
            crop_box = cc[1]
            crop_size = (crop_box[2] - crop_box[0])*(crop_box[3] - crop_box[1])
        else:
            print("no crop control string found")
    
    row_name = folder
    
    # Push into the folder in for loop
    os.chdir('.\\' + folder)
    print('processing images in ' + folder)
    
    # get list of file (image) names in current folder
    files = os.listdir('.')
    
    for file in files:
        # mount image for extraction
        im = Image.open(file)
        
        # Crop image acording to crop control
        im = im.crop(crop_box)
        
        # makes a list of colors (r,g,b) together with there frequency it is a list of tuples 
        # [(count,color)]
        image_colors = im.getcolors(crop_size)
        
        #Build row name. This is a string that will appear at the left most colum of the csv. One 
        # row per image.
        row_name = row_name + '_' + file.split('.')[0]
        
        # start to build the row that will be written. 
        csv_row = [row_name]
        
        # Here we loop over the colors of interest 
        for target_color in target_colors:
            for image_color in image_colors:
                if np.array_equal(image_color[1],target_color):
                    # add color count to the row
                    csv_row.append(image_color[0])
                    break
            else:
                csv_row.append(0)
        # Write the row info to the csv_file
        csv_rows.append(csv_row)
        
    # End for loop over all the files in the folder and we move on to the next folder. 
    #Now we take the information in the list of rows and add it to the csv.

    os.chdir(orignial_directory)
    with open('color_data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_rows)
    os.chdir(desired_directory)
    # We continue this way till we have looped through all folders. 
# End loop over folders
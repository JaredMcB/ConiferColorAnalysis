from PIL import Image
import numpy as np
import os
import pandas as pd
import csv

import Target_colors

orignial_directory = os.getcwd()
os.chdir('G:\\first HW growth chamber photos for Python\\Official HeatWave Start April 30 2018\\April 1 2019 Chamber 1 Canon')
filename = '2981 C1 W-HW 4 water.JPG'
#print (img)
img = Image.open(filename)
size = img.size
pix_val = img.getcolors(size[0]*size[1])
img.show()

rowname = filename.split('.')[0]
row = [rowname]

num_target_colors = len(target_colors)

for set in pix_val:
    for i in range(num_target_colors):
        if np.array_equal(set[1][:3],target_colors[i]):
            row.append(set[0])
        else:
            row.append(0)
rows = [row]
os.chdir(orignial_directory)
with open('Target_Color_counts.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)

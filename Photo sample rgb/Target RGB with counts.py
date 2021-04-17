from PIL import Image
import numpy as np
import os
import pandas as pd
import csv

orignial_directory = os.getcwd()
os.chdir('G:\\first HW growth chamber photos for Python\\Official HeatWave Start April 30 2018\\April 1 2019 Chamber 1 Canon')
filename = '2981 C1 W-HW 4 water.JPG'
#print (img)
img = Image.open(filename)
size = img.size
pix_val = img.getcolors(size[0]*size[1])
img.show()

#print (pix_val)
pix_valR = []
pix_valG = []
pix_valB = []
pix_valcount = []

for set in pix_val:
    pix_valR.append(set[1][0])
    pix_valG.append(set[1][1])
    pix_valB.append(set[1][2])
    pix_valcount.append(set[0])

rowname = filename.split('.')[0]

rowR = [rowname+'R'] + pix_valR
rowG = [rowname+'G'] + pix_valG
rowB = [rowname+'B'] + pix_valB
rowcounts = [rowname+'Count'] + pix_valcount
rows = [rowR,rowG,rowB,rowcounts]

os.chdir(orignial_directory)
with open('Picture_pixels.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)










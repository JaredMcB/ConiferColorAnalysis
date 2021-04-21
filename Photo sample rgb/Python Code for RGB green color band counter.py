import csv
import os
from Target_colors import target_colors_grn, target_colors_brn
import numpy as np
from PIL import Image

original_directory = os.getcwd()
pictures_main_directry = 'E:\\first HW growth chamber photos for Python\\Official HeatWave Start April 30 2018 cropped versions'
os.chdir(pictures_main_directry) # This is the main directory
folderslist = os.listdir()
for folder in folderslist:
    os.chdir(folder) # move into folder directory
    fileslist = os.listdir()
    for filename in fileslist:
        # filename = '2981 C1 W-HW 4 water.JPG'
        #print (img)
        img = Image.open(filename)
        size = img.size
        pix_val = img.getcolors(size[0]*size[1])
        img.show()
        
        rowname = filename.split('.')[0]
        row = [rowname]
        
        num_target_colors = len(target_colors_brn)
        
        for i in range(num_target_colors):
            for set in pix_val:
                if np.array_equal(set[1][:3],target_colors_brn[i]):
                    row.append(set[0])
                    break
            else:
                row.append(0)
        rows = [row]
        os.chdir(original_directory)
        with open('Target_Color_Brn_counts.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)
        os.chdir(pictures_main_directry+"\\"+folder)
    os.chdir(pictures_main_directry)

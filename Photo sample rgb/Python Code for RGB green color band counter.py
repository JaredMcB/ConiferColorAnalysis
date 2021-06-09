import csv
import os
from Target_colors import target_colors_grn, target_colors_brn
import numpy as np
from PIL import Image

# Save current directory so we can access and add to the CSV file in which we 
# will be placeing the data
original_directory = os.getcwd()

# The main directory which holds the pictures and we advance to the directory 
pictures_main_directry = "D://DCIM"
os.chdir(pictures_main_directry) # This is the main directory

# Get list of subdirectories
folderslist = os.listdir()

# Loop over lists of directories
for folder in folderslist[0:1]:
    
    # move into folder directory
    os.chdir(folder)
    
    # Get file list from directory
    fileslist = os.listdir()
    
    # Loop over these files
    for filename in fileslist[0:4]:
        
        # get file image and size
        img = Image.open(filename)
        size = img.size
        
        # gets rgb of each pixel list of colors together with the count of 
        # expression of that color
        pix_val = img.getcolors(size[0]*size[1])
        img.show()
        
        # Form the first three colums of the CSV
        # folder name, sequention designator, plant name
        rowname = filename.split('.')[0]
        row = [folder, rowname[0:4], rowname[5:]]
        
        # Get length of target colors
        num_target_colors = len(target_colors_grn)
        
        # Loop over target colors
        for i in range(num_target_colors):
            
            # loop over colors in picture
            for set in pix_val:
                
                # Test if color is a target color
                if np.array_equal(set[1][:3],target_colors_grn[i]):
                    # If so add to row
                    row.append(set[0])
                    
                    #otherwise skip and place 0 in row
                    break
            else:
                row.append(0)
                
        # Make row in to a list (of one row)        
        rows = [row]
        
        # go back to original directory with CSV
        os.chdir(original_directory)
        
        # Open CSV and add the row we crafted
        with open('Target_Color_Grn_counts.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)
            
        # Go back to specific folder directory for the next file    
        os.chdir(pictures_main_directry+"\\"+folder)
        
    # Got back to picture directory for next folder  
    os.chdir(pictures_main_directry)
    
    
    
    

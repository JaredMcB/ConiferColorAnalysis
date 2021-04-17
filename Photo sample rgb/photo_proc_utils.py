# -*- coding: utf-8 -*-
"""
photo_proc_utils.py
===================

Created on Wed Jan  6 09:46:31 2021

Description: This module contains functions used form extracting color data
from photos. 






@author: JaredMcBride
"""

# Module of functions for extracting target colors from photographs.

from PIL import Image
import numpy as np
import os
import pandas as pd
import csv





def extract_color_data(photofile,
                       csvfile,
                       target_colors)
    """
    This function gets the number that each target color (RGB) appears in a
    photo and outputs the data in a csv file. The row name is the name of the
    photo file and the columns are the colors of interest (in the oreder given)
    
    Its inputs are 
        (1) the file name of the photo (string),
        (2) the file name of the csv file in which the data will be stored (string),
        (3) the list of colors of interest as a list of np.arrays. 
        
    To run ???
    
    """   
 
    
def get_targetcolors(csvfile):
    """
    This function takes a csv file in which each row is an the RGB color (three
    colums). It then produces a list of np.arrays of the RGB colors. This list
    is formated appropriately to serve as the input of 'extract_color_data'.
    
    












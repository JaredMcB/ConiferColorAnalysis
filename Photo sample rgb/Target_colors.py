import csv
import numpy as np

target_colors_grn = []
with open('Grns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        target_colors_grn.append(np.array([int(row[0]),int(row[1]),int(row[2])]))


target_colors_brn = []
with open('Brns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        target_colors_brn.append(np.array([int(row[0]),int(row[1]),int(row[2])]))
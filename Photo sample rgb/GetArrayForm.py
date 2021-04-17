import csv
import numpy as np
colors_brn = []
with open('Brns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        colors_brn.append(np.array([int(row[0]),int(row[1]),int(row[2])]))

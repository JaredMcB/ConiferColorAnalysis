import csv
import numpy as np

target_colors_grn = [np.array([173, 202, 184]),
                    np.array([191, 206, 194]),
                    np.array([167, 189, 177]),
                    np.array([186, 197, 185]),
                    np.array([176, 189, 176]),
                    np.array([188, 201, 197]),
                    np.array([177, 192, 188]),
                    np.array([183, 205, 194]),
                    np.array([160, 218, 179]),
                    np.array([162, 228, 184]),
                    np.array([173, 220, 145]),
                    np.array([208, 222, 187]),
                    np.array([188, 225, 148]),
                    np.array([196, 214, 164]),
                    np.array([188, 209, 155]),
                    np.array([183, 206, 149]),
                    np.array([208, 209, 171]),
                    np.array([198, 200, 155]),
                    np.array([210, 206, 158]),
                    np.array([195, 198, 168]),
                    np.array([187, 197, 146]),
                    np.array([202, 199, 167]),
                    np.array([197, 185, 172]),
                    np.array([209, 204, 189]),
                    np.array([190, 198, 196]),
                    np.array([186, 187, 177]),
                    np.array([196, 191, 182]),
                    np.array([196, 188, 183]),
                    np.array([203, 196, 188]),
                    np.array([191, 184, 175]),
                    np.array([187, 188, 188])]


target_colors_brn = []
with open('Brns.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        target_colors_brn.append(np.array([int(row[0]),int(row[1]),int(row[2])]))
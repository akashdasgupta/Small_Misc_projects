# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:15:35 2020

@author: akash
"""

import csv
from matplotlib import pyplot as plt
import os

path = r"C:\Users\akash\Downloads\OneDrive_1_19-11-2020"

# Finds the files: 
filelist = []
for path, directories, files in os.walk(path):
     for file in files:
         if file.startswith("long") and file.endswith('in.txt'):
             filelist.append(os.path.join(path, file))

#Opens and plots: 
for filename in filelist:
    with open(filename) as file:
        wavel = []
        counts = []
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            try:
                wavel.append(float(row[0]))
                counts.append(float(row[1]))
            except:
                pass
    plt.plot(wavel,counts)

plt.xlim((700, 900))


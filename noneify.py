
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 2022

@author: Cristian Ortega Singer
"""

import csv
import os
from collections import OrderedDict

datapath = "./metadata" #replace with path to directory where the data sets to be processed are stored
donepath = "../done" #replace with path to directory where the finished data sets will be stored

#initiating variables
os.chdir(datapath)
cwd = os.getcwd()
files = []
files = os.listdir(cwd) #get list with all files that will be processed
rows = []
header = []

for file in files: #iterating through all files
    print(file)
    with open(file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        header = reader.fieldnames #define header for new file
        for row in reader: #read csvfiles line by line
            nrow = OrderedDict(row.copy()) #make a working copy
            for x in nrow: #iterate through all cells in current row and check for known cases that should be replaced by "None"
                if nrow[x] == None or nrow[x] == "None" or nrow[x] == "none" or nrow[x] == "" or nrow[x] == "Keine Angabe" or nrow[x] == "Nicht angegeben" or nrow[x].isspace():
                    nrow[x] = "None" #if one of the cases is true, replace value of cell with "None"
            rows.append(nrow) #append edited row to list "row"
    os.chdir(donepath) #change directory to place where the edited file should be saved
    filename = "none-" + file #define name of new file
    with open(filename, "w", newline="", encoding="utf-8") as csvfile: #create file and write list "rows" to csv
        writer = csv.DictWriter(csvfile, fieldnames= header)

        writer.writeheader()
        for x in rows:
            writer.writerow(x)
    rows = []
    os.chdir("." + datapath) #change directory back to place where the data sets to be processed are stored

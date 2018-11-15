import csv
import numpy as np
from array import array
import ConfigParser
from os import listdir, walk
from os.path import isfile, join
import csv
import sys
import argparse

# passes directory and filename to program for naming

def percentage(input_list):
    float_list = []
    output_list = []
    for item in input_list:
        float_list.append(float(item))
    for item in float_list:
        output_list.append((100/max(float_list)*item))
    return output_list

parser = argparse.ArgumentParser(description = 'Produce .txt file output from _extern.inf')
parser.add_argument ('directory', help = 'Folder Name', action = 'store')
parser.add_argument('name', help = 'name the thing', action = 'store')
parser.add_argument('s_v', help = 'starting voltage', action = 'store')
parser.add_argument('e_v', help = 'end voltage', action = 'store')
parser.add_argument('inc', help = 'voltage increment', action = 'store')
args = parser.parse_args()
directory = args.directory
title = args.name
s_v = args.s_v
e_v = args.e_v
inc = args.inc 
# title = 'M_var' # title for position (0,0)
# title = 'Z_var'
# title = 'S_var'
# title = 'RecWT'
# title = 'tst'

volt_list = range(int(s_v), int(e_v) + int(inc), int(inc)) # voltage range for list ((1,0),(-1,0))

# creating first line of array for correct 

title_list = []
title_list.append(title)
for volt in volt_list:
    title_list.append(str(volt) + 'V')


file_list = []

data = []

for files in listdir(directory):
    # print(files)
    if files.endswith('.txt'):
        file_list.append(directory + '\\' + files)

# create array for data to be added

array = []
        
# pulling data out of the individual challenger files

for item in file_list:
    with open(item, 'r') as txt_file:
        for x in range(0,25):
            if x ==0 :
                ccs = []
                pc_int = []
                for line in txt_file:
                    data_list = (line.strip().split('\t'))
                    ccs.append(data_list[0])
                    pc_int.append(data_list[1])

                array.append(ccs)
                array.append(percentage(pc_int))


            pc_int = []
            for line in txt_file:
                
                data_list = (line.strip().split('\t'))
                print(data_list)
                pc_int.append(data_list[1])
                array.append(pc_int)
                print(pc_int)
length = len(array)

# writing out the files as tab separated array


filename = title + '.txt'
path_name = join(directory, filename)

with open(path_name, 'w') as write_file:
    writer = csv.writer(write_file, delimiter = '\t', lineterminator = '\n')
    
    writer.writerow(title_list)
    writing_list = []    
    writing_list.append(title_list)
    writing_list.append(array[0])
    for x in range(1,len(array),2): 
        writing_list.append(array[x])

    write_length = len(writing_list)
    ziplist = []
    for x in range(1,write_length):
        ziplist.append(writing_list[x])  

    
    rows = zip(*ziplist)
    for row in rows:
        writer.writerow(row)
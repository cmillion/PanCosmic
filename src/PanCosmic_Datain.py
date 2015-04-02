#!/usr/bin/python

import os
import urllib2
import re
import csv

os.remove('Pancosmic_Files.txt')
f = open('Pancosmic_Files.txt','w')

print('Select Data from Mars Exploration Rover 1 or 2: ')
rover_num2 = raw_input()
rover_num1 = int(rover_num2)

rover1 = 'opportunity'
rover2 = 'spirit'

if rover_num1 == 1:
    rover = rover1
elif rover_num1 == 2:
    rover = rover2
else:
    print('Press enter to fail')

print('Enter the Initial SOL day:')
print('Example - 0021 or 0002')
initsol = raw_input()
initsol_int = int(initsol)
initsol_str = str(initsol)
print('Enter the Final SOL day:')
print('Example - 2000 or 0101')
finsol = raw_input()
finsol_int = int(finsol)
finsol_int = finsol_int + 1
finsol_str = str(finsol)

day=[]
URLi=[]
for i in range(initsol_int,finsol_int):
    solday = "{0:0>4}".format(i)
    URL = 'http://pds-imaging.jpl.nasa.gov/data/mer/%s/mer%1spo_0xxx/data/sol%4s/rdr/'%(rover, rover_num1, solday)
    print(URL)
    out = urllib2.urlopen(URL)
    code = out.read()
    regex1 = re.compile('(?<=<a.href=")...........................\.img')
    regex2 = re.compile('(?<=data/sol)....(?=/rdr/)')
    file_names = re.findall(regex1,code)
    filenames = str(file_names)
    number_files = len(filenames)/35
    start=0
    end=35
    read_file = []
    for x in range(0,number_files):
        dayzz = re.findall(regex2,URL)
        dayz = str(dayzz)
        day1 = dayz[2:-2]
        day.append(day1)
        URLz = URL
        URLi.append(URLz)
        start = start+35
        end = end+35
        read_filex = filenames[start:end]
        read_file.append(read_filex)
    readfile = []
    time = []
    prod = []
    site = []
    pos = []
    eye =[]
    filt = []
    for y in range(0,number_files):
        readfile1=read_file[y][2:-2]
        time1 = read_file[y][4:-22]
        prod1 = read_file[y][13:-19]
        site1 = read_file[y][16:-17]
        pos1 = read_file[y][18:-15]
        eye1 = read_file[y][25:-9]
        filt1 = read_file[y][26:-8]
        readfile.append(readfile1)
        time.append(time1)
        prod.append(prod1)
        site.append(site1)
        pos.append(pos1)
        eye.append(eye1)
        filt.append(filt1)
    g = open('Pancosmic_Files.txt','a')
    for z in range(0,number_files):
        g.write(day[z]+','+time[z]+','+prod[z]+','+site[z]+','+pos[z]+','+eye[z]+','+filt[z]+','+readfile[z]+','+URLi[z]+'\n')
    del read_file[:]
    del readfile[:]
    del time[:]
    del prod[:]
    del site[:]
    del pos[:]
    del eye[:]
    del filt[:]
    del day[:]
    del URLi[:]
    lines = file('Pancosmic_Files.txt','r').readlines()
    del lines[-1]
    os.remove('Pancosmic_Files.txt')
    file('Pancosmic_Files.txt','a').writelines(lines)

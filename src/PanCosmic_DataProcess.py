#!/usr/local/bin/python2.7
"""
PanCosmic_DataProcess.py enables the parsing of data from the larger volume of
data collected using the PanCosmic_Datain.py script. This Script enables
filtering based on parameters such as the solar day, product, site, position,
and filter. The resulting URL's for the selected images will be written to the
PanCosmic_URLs.txt text file.
"""
import numpy as np
import pandas as pd
import urllib2
import os

print('Fine Parsing Commencing...')

data2 = pd.read_csv('Pancosmic_Files.txt')
data2.columns = ['sol day','time','prod','site','pos','eye','filter','File name','URL']
#print data[:10]
data = pd.DataFrame.drop_duplicates(data2)

print('Enter the starting day number: ')
daynum1=int(raw_input())
print('Enter the ending day number: ')
daynum2=int(raw_input())
print('Enter the product: ')
prod=str(raw_input())
print('Enter the filter: ')
filt=int(raw_input())

sel = data[((data['sol day'] >= daynum1) & (data['sol day'] <= daynum2)) & (data['prod'] == prod) & (data['filter'] == filt)]
url = sel['URL'].tolist()
fname = sel['File name'].tolist()


full_url=[]
for a in range(0,len(url)):
    full_url1= url[a]+fname[a]
    full_url.append(full_url1)
f = open('PanCosmic_URLs.txt','w')
last = len(full_url)
for b in range(0,last):
    f.write(full_url[b]+'\n')

print('Fine parsing completed....')

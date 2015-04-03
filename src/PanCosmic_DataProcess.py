import numpy as np
import pandas as pd
import urllib2
import os

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

read = urllib2.urlopen(full_url[20])
img = read.read()
#print html
f=open('Pancosmic_img.txt','w')
f.write(img)

g = open('Pancosmic_img.txt','r')
x = g.readlines()
h = open('Pancosmic_Meta.txt','w')
for y in range(0,480):
    h.write(x[y])

i = open('Pancosmic_binary.txt','w')
for z in range(481,2030):
    aa = (''.join(format(ord(zz), 'b') for zz in x[z]))
    i.write(aa+'\n')
"""
bob =  x[20]
joe = (''.join(format(ord(z), 'b') for z in bob))
print joe
"""

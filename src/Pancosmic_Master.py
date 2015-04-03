#!/usr/local/bin/python2.7
"""
Pancosmic_Master.py allows for one script to controll all other scripts in the
PanCosmic project. As long as all PanCosmic scripts exist in the same directory
as the master script it will be able to execute all scripts in the correct
order.
"""
import os

file_name1 = 'Datain'
file_name2 = 'DataProcess'

for x in range(0,2):
    if x == 0:
        file_name = file_name1
    elif x == 1:
        file_name = file_name2
    else:
        print('Dire consequences')
    os.system('./PanCosmic_%s.py'%(file_name))

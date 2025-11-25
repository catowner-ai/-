# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:00:05 2021

@author: OfficePC
"""
import os
def filetest(file):
    line = None
    if os.path.isfile(file):
        filedata = open(file,'r')
        for note in filedata:
            print(note)
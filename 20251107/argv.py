# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 13:17:25 2025

@author: USER
"""

from PIL import Image
import pytesseract
import os
import sys
import glob
 
print(sys.argv[1])

print(sys.argv[2])

print(sys.argv[3])

for infile in sys.argv[1:]:
    print("process")
    f,e=os.path.splitext(infile)
    outfile=f+".png"
    if infile !=outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('Cannot convert',infile)
print("end")  
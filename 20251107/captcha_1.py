# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:17:57 2023

@author: USER
"""

from PIL import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('./image1.jpg')

print(img.format, img.size , img.mode)

img.show()

# img = img.convert('L')
# ans=pytesseract.image_to_string(img)
# print(ans)
# print("end")


#%%

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


         
#%%
import os
import sys
import glob
 

size=(128,128)
for infile in glob.glob("photo/*.jpg"):
    f,ext=os.path.splitext(infile)
    img = Image.open(infile)
    # img.thumbnail(size,Image.ANTIALIAS)
    img.thumbnail(size,Image.LANCZOS)
    img.save(f+"conver"+".jpg")
img.show() 
 
#%%

im=Image.open("photo/monkey1.jpg")
im.show()

box=(100,100,300,300)
region = im.crop(box)
region.show() 

#%%


region = region.transpose(Image.ROTATE_90)
im.paste(region,box)
im.show()  

#%%

r,g,b = im.split()



im=Image.merge("RGB",(r,g,b))


#%%
# out=im.resize(128,128)
im=Image.open("photo/monkey1.jpg")

out=im.resize([128,128])
out.show()

#%%

out=im.rotate(180)

out.show()



#%%

cmyk=im.convert("CMYK")
gray=im.convert('L')

gray.show()
cmyk.show()


#%%

from PIL import ImageFilter
from time import sleep

im=Image.open("photo/monkey2.jpg")


out=im.filter(ImageFilter.DETAIL)
contour=im.filter(ImageFilter.CONTOUR)
edge_hance=im.filter(ImageFilter.EDGE_ENHANCE())

im.show()

sleep(5)

out.show()

sleep(5)
contour.show()

sleep(5)
edge_hance.show()

#%%

from PIL import ImageEnhance
im=Image.open("photo/abba.png")
im.show()

imgEH=ImageEnhance.Contrast(im)
imgEH.enhance(1.5).show("50% more contrast")




            
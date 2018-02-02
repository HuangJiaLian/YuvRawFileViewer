#!/usr/bin/python

import Image
import sys
from struct import *
import array

if len(sys.argv) != 5:
        print "***** Usage syntax Error!!!! *****\n"
        print "Usage:"
        print "python yuvViewer.py filename w h format(YUV420P)"
        sys.exit(1) 
else:
        pass

image_name = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])
format = sys.argv[4]
y = array.array('B')

f_y = open(image_name, "rb")

image_out = Image.new("L", (width, height))
pix = image_out.load()

print "image_name:",image_name,"width=",width,"height=",height

if format =="YUV420P":
    for i in range(0,height):
      for j in range(0, width):
        y.append(ord(f_y.read(1)));
        Y_val = y[(i*width)+j]
        pix[j, i] = Y_val 

image_out.save("out.jpeg")
image_out.show()
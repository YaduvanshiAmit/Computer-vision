# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:02:00 2021

@author: Joel
"""

"""
Resizing the image

"""
import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
print(img.shape)

cv2.imshow("Image",img)
cv2.waitKey(0)

## Resize the image
# in opencv width,height
imgResize = cv2.resize(img,(1000,500)) 
print(imgResize.shape)

cv2.imshow("imgResize",img)
cv2.waitKey(0)

## image Cropped
# here hight ,width[start:end]
imgCropped = img[46:119,352:495]
cv2.imshow("imgCropped",img)
cv2.waitKey(0)

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:45:13 2021

@author: Joel
"""

"""
Play with image

"""
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

## Convert the image into gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.imshow("Gray Image",imgGray)

## Convert the image in blur

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # kernel size always in odd number
cv2.imshow("Blur Image",imgBlur)

## convert the image in canny
## it is edge detector 
imgCanny = cv2.Canny(img,150,200)
cv2.imshow("Canny Image",imgCanny)

# sometimes canny cant detect the edge properly then we use dialation to make more thickness
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Dialation Image",imgDialation)



imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded Image",imgEroded)

# waitkey is impotant to give 
cv2.waitKey(0)

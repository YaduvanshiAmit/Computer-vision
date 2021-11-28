# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:52:43 2021

@author: Joel
"""

"""
from many image pic ine image

"""
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

# nw our task to pic one card from that 
width,height = 250,350
# here we define the points of which image we need to wrap
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# here we define each point belong to whih corner

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
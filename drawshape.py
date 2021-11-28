# -*- coding: utf-8 -*-
"""
e Created on Mon Apr 19 21:16:18 2021

@author: Joel
"""

"""
Make some circle square

"""
import cv2
import numpy as np

# here we created a blank image zeros means black
img = np.zeros((512,512,3),np.uint8)

# if u want to do whole blue in color

# img[:] = 255,0,0

#print(img)

print(img.shape)
# create line in  image
# 1.name of image
# 2. Starting point width,height
# 3. end point      width,height
# 4. color
# 5. width

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# create a rectangle

cv2.rectangle(img,(0,0),(250,250),(0,0,255),5)# if u want to filled your rectangle use
# in thinckness place cv2.FILLED

# create a circle

cv2.circle(img,(180,60),50,(255,0,0),6)

# Nw put text

cv2.putText(img,"YADUVANSHI",(2,240),cv2.FONT_HERSHEY_COMPLEX,1,(150,255,150),3)


cv2.imshow("Image",img)
cv2.waitKey(0)
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 01:26:40 2021

@author: Joel
"""

## Face detection 

import cv2

faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
#img = cv2.imread('Resources/lena.png')
#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150) # britness
while True:
    success, img = cap.read()
    
    faces = faceCascade.detectMultiScale(img,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#cv2.imshow("Result", img)
#cv2.waitKey(0)
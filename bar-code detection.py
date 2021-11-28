# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:44:05 2021

@author: Joel
"""

import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('Resources/barcode')
# =============================================================================
# # =============================================================================
# =============================================================================
# =============================================================================
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10,200)
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

while True:
    

    #sucess,img = cap.read()
    img = cv2.imread('Resources/emp.jpg')
    #img = cv2.resize(img,(500,500)) 
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                                0.9,(255,0,255),2)
        
    cv2.imshow('Result',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 09:36:33 2021

@author: Amit
"""
# read about face regonition liabrary

# https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

##############################################################################
"""
1. Encode a picture using the HOG algorithm to create a simplified version of the image. 
Using this simplified image, find the part of the image that most looks like a generic HOG encoding
 of a face.
 

2. Figure out the pose of the face by finding the main landmarks in the face. 
Once we find those landmarks, use them to warp the image so that the eyes and mouth are centered. 


3. Pass the centered face image through a neural network that knows how to measure features of
 the face. Save those 128 measurements.
 
 
4. Looking at all the faces we’ve measured in the past, see which person has the closest 
measurements to our face’s measurements. That’s our match! 

"""
##############################################################################

import cv2
import face_recognition

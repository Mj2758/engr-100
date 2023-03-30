# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:16:57 2019

@author: Jakob.Spurgat
"""

import cv2
import numpy as np

def nothing(x):
    pass

#lower = np.array([85, 200, 200])
#upper = np.array([105, 255, 255])
try:
    cap.release()
except:
    pass
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)


cv2.namedWindow('image')
cv2.createTrackbar('HU', 'image', 72, 180, nothing)
cv2.createTrackbar('HL', 'image', 114, 180, nothing)
cv2.createTrackbar('SU', 'image', 119, 255, nothing)
cv2.createTrackbar('SL', 'image', 230, 255, nothing)
cv2.createTrackbar('VU', 'image', 63, 255, nothing)
cv2.createTrackbar('VL', 'image', 232, 255, nothing)

"hello there general kenobi"

k = 255
while k != 27:
    ret, frame = cap.read()
    if ret:
        hu = cv2.getTrackbarPos('HU', 'image')
        hl = cv2.getTrackbarPos('HL', 'image')
        su = cv2.getTrackbarPos('SU', 'image')
        sl = cv2.getTrackbarPos('SL', 'image')
        vu = cv2.getTrackbarPos('VU', 'image')
        vl = cv2.getTrackbarPos('VL', 'image')
        lower = np.array([min(hu, hl), min(su, sl), min(vu, vl)])
        upper = np.array([max(hu, hl), max(su, sl), max(vu, vl)])
        
        frame = cv2.resize(frame, (640, 480))
        hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvframe, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('image', mask)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()

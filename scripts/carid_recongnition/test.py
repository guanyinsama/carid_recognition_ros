#!/usr/bin/python
#coding=utf-8
# from  import *
import sys
sys.path.append('../')
from scripts import *
import cv2
import time
img= cv2.imread("test2.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
t1=time.time()
a=HyperLPR_plate_recognition(img)
t2=time.time()
print('ke',t2-t1,a)
print(img.shape)
# cv2.rectangle(img, (img.shape[1]-a[0][2][0],img.shape[0]-a[0][2][1] ), (img.shape[1]-a[0][2][2],img.shape[0]-a[0][2][3] ), (0, 255, 0), 2)
# cv2.imshow("image", img)
# cv2.waitKey(0)
cv2.rectangle(img, (a[0][2][0],a[0][2][1] ), (a[0][2][2],a[0][2][3] ), (0, 255, 0), 2)
cv2.imshow("image", img)
cv2.waitKey(0)

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('./photos/cat.jpeg')
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#gray image
gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#BGR to HSV
hsv=cv.cvtColor(resized_img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
#BGR to LAB
lab=cv.cvtColor(resized_img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)
#BGR to RGB
rgb=cv.cvtColor(resized_img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
#BGR to LUV
luv=cv.cvtColor(resized_img,cv.COLOR_BGR2LUV)
cv.imshow('luv',luv)
#BGR to HLS
hls=cv.cvtColor(resized_img,cv.COLOR_BGR2HLS)
cv.imshow('hls',hls)
#BGR to XYZ
xyz=cv.cvtColor(resized_img,cv.COLOR_BGR2XYZ)
cv.imshow('xyz',xyz)
#BGR to YUV
yuv=cv.cvtColor(resized_img,cv.COLOR_BGR2YUV)
cv.imshow('yuv',yuv)
#BGR to YCrCb
ycrcb=cv.cvtColor(resized_img,cv.COLOR_BGR2YCrCb)
cv.imshow('ycrcb',ycrcb)
#img in matplotlib
plt.imshow(resized_img)
plt.show()

cv.waitKey(0)

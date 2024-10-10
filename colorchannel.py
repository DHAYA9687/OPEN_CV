import cv2 as cv
import numpy as np
#read the image
img=cv.imread('./photos/image.jpg')
#resize the image
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized_img)
#blank image 
blank=np.zeros(resized_img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)
#split the image
b,g,r=cv.split(resized_img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)
print(resized_img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
#merge the image
merged=cv.merge([b,g,r])
cv.imshow('merged',merged)
#merge the split color with blank image
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)
cv.waitKey(0)
import cv2 as cv
import numpy as np
#read the image
img=cv.imread('../photos/cat.jpeg')
#resize the image
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized_img)
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

cv.waitKey(0)


import cv2 as cv
import numpy as np
#read the image
img=cv.imread('../photos/D.photo.jpg')
cv.imshow('Dhaya',img)

# convert the image to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#blur the iamge 
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
#edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)
#dilate the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)
#erode the image
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)
#resize the image
resize=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resize)
#crop the image
crop=img[50:200,200:400]
cv.imshow('Crop',crop)

cv.waitKey(0)

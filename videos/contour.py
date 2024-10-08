import cv2 as cv
import numpy as np
img=cv.imread('../photos/D.photo.jpg')
cv.imshow('Dhaya',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#blur the image
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
#edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)
contour,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#RETR_LIST-->retrive all the contours(mode)
#CHAIN_APPROX_NONE-->retrive all the contours
#CHAIN_APPROX_SIMPLE-->retrive meaningful contours if its a line two contour is enough to represent it
print(f'{len(contour)} contours found')
cv.waitKey(0)
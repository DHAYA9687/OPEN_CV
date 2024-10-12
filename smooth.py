import cv2 as cv
import numpy as np
#read the image
img=cv.imread('./photos/image.jpg')
#resize the image
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized_img)
blur=cv.blur(resized_img,(3,3))
cv.imshow('blur',blur)
#Gaussian blur
gauss=cv.GaussianBlur(resized_img,(3,3),0)
cv.imshow('gauss',gauss)
#median blur
median=cv.medianBlur(resized_img,3)
cv.imshow('median',median)
#bilateral blur(Retain the edges in the image)
bilateral=cv.bilateralFilter(resized_img,10,35,25)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)
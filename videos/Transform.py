import cv2 as cv
import numpy as np
#read the image
img=cv.imread('../photos/D.photo.jpg')
cv.imshow('Dhaya',img)
# resize the image 
resize_img = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('resize',resize_img)
#transorm the image 
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# -x -->left
# -y -->up
# x -->right
# y -->down
translated=translate(resize_img,-100,100)
cv.imshow('translated',translated)
#rotate the image
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(resize_img,45)
cv.imshow('rotated',rotated)
#flip the image
#0-->flip vertically
#1-->flip horizontally
#-1-->flip both vertically and horizontally
flip=cv.flip(resize_img,1)
cv.imshow('flip',flip)
cv.waitKey(0)

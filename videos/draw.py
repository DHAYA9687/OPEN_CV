import cv2 as cv
import numpy as np
#read the image
img=cv.imread('../photos/D.photo.jpg')
cv.imshow('Dhaya',img)
#paint the dummy image
blank=np.zeros((500,500,3),dtype='uint8')
blank[:]=255,0,0

#paint the certain portion
blank[200:300,300:400]=0,255,0

#draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)#tthickness=cv.filled
cv.imshow('Blank',blank)
# draw a circle
cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=cv.FILLED)
cv.imshow('circle',blank)
# draw a line
cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness=3)
cv.imshow('line',blank)
# write text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
cv.waitKey(0)
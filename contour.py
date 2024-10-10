import cv2 as cv
import numpy as np
img=cv.imread('./photos/cat.jpeg')
resized_img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#blank image 
blank=np.zeros((500,500,3),dtype='uint8')

if resized_img is None:
    print('image not found')
else:
    cv.imshow('CAT',resized_img)
gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#blur the image
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# #edge cascade
canny=cv.Canny(blur,125,175)
# cv.imshow('canny',canny)
# #threshold
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contour,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# print(contour) get form the contours
cv.drawContours(blank,contour,-1,(0,255,255),0)
cv.imshow('contour_blank',blank)
# #RETR_LIST-->retrive all the contours(mode)
# #CHAIN_APPROX_NONE-->retrive all the contours
# #CHAIN_APPROX_SIMPLE-->retrive meaningful contours if its a line two contour is enough to represent it
print(f'{len(contour)} contours found')
cv.waitKey(0)
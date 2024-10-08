import cv2 as cv

#read the image
img=cv.imread('../photos/D.photo.jpg')

#resize the video
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#resize the image
if img is None:
    print("Error: Could not read the image")
else:
    # Resize the image
    resize_img = rescaleFrame(img)
    cv.imshow('Dhaya', img)
    cv.imshow('resize', resize_img)

#resize the live video
# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)

#read the video
capture=cv.VideoCapture('video1.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    
    cv.imshow('Video Resized',rescaleFrame(frame,scale=0.25))
    if cv.waitKey(10) & 0xFF==ord('d'):
        print("ord",ord('d'))
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)


# #enhance red in the image
# import cv2 as cv
# import numpy as np
# img=cv.imread('../photos/D.photo.jpg')
# img[:,:,:]=np.clip(img[:,:,:]<0,0,img[:,:,:])
# cv.imshow('Dhaya',img)
# cv.imwrite('enhanced.jpg',img)
# cv.waitKey(0)
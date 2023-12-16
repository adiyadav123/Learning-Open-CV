import cv2 as cv

img = cv.imread('OPENCV/images/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)
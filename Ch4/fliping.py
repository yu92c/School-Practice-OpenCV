import cv2 as cv
import numpy as np

img = cv.imread('pic/cb.jpg')
cv.imshow('Original', img)     

flip = cv.flip (img,-1) #0上下顛倒, 1左右, -1上下左右顛倒
cv.imshow('flip',flip)
cv.waitKey(0)
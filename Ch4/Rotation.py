# 3. Rotation --------------------------------------------------------------------------------
import cv2 as cv
import numpy as np

img = cv.imread('../pic/cb.jpg')
cv.imshow('oringal', img)     

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
       rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) #45往左倒 , -45向右倒。
cv.imshow('Rotated', rotated)

cv.waitKey(0)
# 仿射轉換（Affine Transformations）
# 改變影像的位置、角度、大小、形狀，但會保持線性結構（也就是直線還是直線，平行還是平行）。
# 圖像繞中心或任意點旋轉
import cv2 as cv
import numpy as np

img = cv.imread('pic/cb.jpg')
cv.imshow('original', img)
 

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
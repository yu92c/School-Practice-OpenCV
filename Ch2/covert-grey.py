import cv2 as cv
img = cv.imread('pic/cb.jpg')
cv.imshow('img', img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey)

cv.waitKey(0)
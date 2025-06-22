import cv2 as cv
img = cv.imread('pic/cb.jpg')             # loading image.
cv.imshow('cb', img)         

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# 模糊程度 GaussianBlur(img, (5,5)只能是奇數）

cv.imshow('blur', blur)
cv.waitKey(0)

#cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst

#--------------------------------------------------------------
#| kernel size | 模糊程度 | 說明             |
#| ----------- | -------| -------------- |
#| (3, 3)      | 微模糊  | 幾乎看不出來，但邊緣會稍柔化 |
#| (5, 5)      | 明顯模糊 | 一般人眼可以辨認出柔化效果  |
#| (15, 15)    | 很模糊  | 圖片開始糊掉，看不清細節   |
#| (51, 51)    | 超級模糊 | 幾乎變成一片色塊了      |
#--------------------------------------------------------------


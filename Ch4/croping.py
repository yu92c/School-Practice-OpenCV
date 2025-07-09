import cv2 as cv
import numpy as np

img = cv.imread('pic/cb.jpg')
print("Original size:", img.shape)
cv.imshow('original', img)



crop = img[200:400, 300:500]
print('crop:',crop.shape)
cv.imshow('crop',crop)
cv.waitKey(0)   

# 原圖 img[y][x]：
#+--------------------------------------+
#|                                      |
#|   y=80 → +----------------------+    |
#|          |                      |    |
#|          |     裁切的區塊       |    |
#|   y=100→ +----------------------+    |
#|          x=300             x=400     |
# +--------------------------------------+
# 大小為 (高 20、寬 100)


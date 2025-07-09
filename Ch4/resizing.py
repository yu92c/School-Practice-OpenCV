import cv2 as cv
import numpy as np 

img = cv.imread('pic/cb.jpg') # loading image.
cv.imshow('original', img)
print('Original:', img.shape) # original img size 

resize = cv.resize(img,(300,200), interpolation=cv.INTER_AREA)
print('resize:',resize.shape) # after resize 

# interpolation=cv.INTER_AREA --> 縮小圖片
              # cv.INTER_LINEAR --> 圖片放大
              # cv.INTER_CUBIC --> 圖片放大
              # | 插值方法名稱       | 對應常數名      | 用途說明         | 特色    |
# | ------------ | ----------------- | --------------- | --------- |
# | 區域插值法     | `cv.INTER_AREA`   |  縮小圖片時最佳   | 降噪效果好、最清晰 |
# | 雙線性插值     | `cv.INTER_LINEAR` | 放大圖片時預設值  | 速度快，畫質普通  |
# | 立方插值（4×4） | `cv.INTER_CUBIC`  | 放大圖更高品質   | 畫質好，但慢    |

cv.imshow('resize', resize)
cv.waitKey(0)
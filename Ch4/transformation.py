
# 2D Affine Transformation in OpenCV 一律使用 2×3 矩陣，這是固定格式
# 因為：輸入是 (x, y, 1)，輸出是 (x', y')。

 
#| Affin Transformation Type   | Description                                                  |
#| ----------------------------| ------------------------------------------------------------ |
#| 1. Translation              | Moves the image in X or Y direction                          |
#| 2. Scaling                  | Enlarges or shrinks the image                                |
#| 3. Rotation                 | Rotates the image around a point                             |
#| 4. Shearing (Skewing)       | Slants the shape of the image in X or Y                      |
#| 5. Reflection               | Mirrors the image across an axis                             |
#| 6. Combination              | You can combine any of the above in one single affine matrix |

import cv2 as cv
import numpy as np

img = cv.imread('pic/cb.jpg')
cv.imshow('cb',img)




# 1. translate----------------------------------------------------------------
def translate(img, x, y):
    translate = np.float32([1,0,x],[0,1,y])
    
    # x: 水平方向要移動多少像素（+往右，−往左）
    # y: 垂直方向要移動多少像素（+往下，−往上）


    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translate, dimensions)

#---------------------------------------------------------------------------------



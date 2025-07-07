# 2D Affine Transformation in OpenCV 一律使用 2×3 矩陣，這是固定格式
# 在 NumPy 或 Python 中，2D 矩陣的索引格式是 ： [ 行 ][ 列 ]
# 因為：輸入是 (x, y, 1)，輸出是 (x', y')。 


#| Affin Transformation Type   | Description                                                  
#| ----------------------------| ------------------------------------------------------------ |
#| 1. Translation              | Moves the image in X or Y direction                          |
#| 2. Scaling                  | Enlarges or shrinks the image                                |
#| 3. Rotation                 | Rotates the image around a point                             |
#| 4. Shearing (Skewing)       | Slants the shape of the image in X or Y                      |
#| 5. Reflection               | Mirrors the image across an axis                             |
#| 6. Combination              | You can combine any of the above in one single affine matrix |

# 1. translate--------------------------------------------------------------------------------

import cv2 as cv
import numpy as np

img = cv.imread('/pic/cb.jpg')
cv.imshow('Original', img)     


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)

#---------------------------------------------------------------------------------
# 搬移座標：像素座標要用矩陣去計算新位置（用 warpAffine()）

# 原本圖片座標
# |A B |
# |C D |
# +----+

# 做平移(右移1格)，像素「位置」改變（搬移座標）
# +-----+
# |  A B|
# |  C D|
# +-----+
#---------------------------------------------------------------------------------
 

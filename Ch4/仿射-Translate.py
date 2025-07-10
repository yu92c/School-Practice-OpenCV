# 仿射轉換（Affine Transformations）
# 改變影像的位置、角度、大小、形狀，但會保持線性結構（也就是直線還是直線，平行還是平行）。
# 平移	將圖像往上下左右移動

import cv2 as cv
import numpy as np

cv.imshow('Original', img)     


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
    #仿射轉換 cv.warpAffine() + 矩陣

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)

# 2D Affine Transformation in OpenCV 一律使用 2×3 矩陣，這是固定格式
# 在 NumPy 或 Python 中，2D 矩陣的索引格式是 ： [ 行 ][ 列 ]
# 因為：輸入是 (x, y, 1)，輸出是 (x', y')。 


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
 

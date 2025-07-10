import cv2
import numpy as np

img = cv2.imread('pic/cb.jpg')
h, w = img.shape[:2]

# 仿射縮放矩陣（Sx = 1.5, Sy = 0.5）
scale_x = 1.5  # 水平放大 1.5 倍
scale_y = 0.5  # 垂直縮小為一半

# 仿射矩陣：只有縮放 + 無平移
M = np.float32([
    [scale_x, 0,       0],
    [0,       scale_y, 0]
])

# 輸出畫布大小要根據縮放後尺寸決定
new_w = int(w * scale_x)
new_h = int(h * scale_y)

scaled_img = cv2.warpAffine(img, M, (new_w, new_h))

cv2.imshow('Original', img)
cv2.imshow('Scaled by Affine', scaled_img)
cv2.waitKey(0)

# 比較
#| 方法                | 函式      | 特點                           |
#| ------------------ | ---------| -------------------------------- |
#| `cv2.resize()`     | 最直接    | 縮放比例 fx / fy；支援補差演算法   |
#| `cv2.warpAffine()` | 用仿射矩陣 | 可以同時結合平移、旋轉、剪切      |

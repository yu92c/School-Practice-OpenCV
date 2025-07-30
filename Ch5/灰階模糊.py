import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# 讀取灰階圖像
img = cv2.imread('pic/rope.png', cv2.IMREAD_GRAYSCALE)


# 3x3 「模糊濾波器（平均濾波器 / 均值濾波器）」的核心架構
# 讓影像變模糊、降低雜訊，也會降低邊緣清晰度。
kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
], dtype=np.float32)
kernel = kernel / kernel.sum()  # 正規化使總和為 1

# 卷積處理
filtered = convolve2d(img, kernel, mode='same', boundary='symm')

# 顯示結果
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Filtered (Blur)")
plt.imshow(filtered, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.waitforbuttonpress() # 等待按下任何鍵或滑鼠點擊

'''
一眼看出：模糊 vs 銳化 的差別
| 類型    | 核心特徵          | 功能          | 核心數值範例                          |
| ----- | ------------- | ----------- | ------------------------------- |
|  模糊核 | 全為正值，通常總和 = 1 | 平均周圍像素，模糊圖像 | `[[1,1,1],[1,1,1],[1,1,1]] / 9` |
|  銳化核 | 中間是大正數，周圍是負值  | 增強邊緣對比，變清晰  | `[[0,-1,0],[-1,5,-1],[0,-1,0]]` |

'''
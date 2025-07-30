
'''
| 項目     | 平均濾波 (`blur`) | 高斯模糊 (`GaussianBlur`) |
| ------ | ------------- | --------------------- |
| 權重分配   | 每個像素等權重    | 中心重、周圍輕（高斯分布）   |
| 模糊效果   | 不自然、死板      | 自然柔順                  |
| 邊緣保留能力 | 差             | 較好                     |
| 去除雜訊   | 普通             | 較有效                   |

'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

# 讀取原始圖片
img1 = cv2.imread('pic/m.png', -1)


# 進行模糊處理
avg_blur = cv2.blur(img1, (9, 9))                     # 平均濾波
gauss_blur = cv2.GaussianBlur(img1, (9, 9), 0)        # 高斯模糊


# 合併顯示
images = [img1, avg_blur, gauss_blur]
titles = ['Original Image', 'Average Blur', 'Gaussian Blur']

plt.figure(figsize=(16, 4))  # 四張圖橫排
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # BGR → RGB
    plt.title(titles[i])
    plt.axis('off')  # 關閉座標軸

plt.tight_layout()
plt.waitforbuttonpress()  # 等待任意鍵或滑鼠點擊

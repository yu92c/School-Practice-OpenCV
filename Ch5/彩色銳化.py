import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取圖片（彩色）
img = cv2.imread('pic/cat.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV 是 BGR，要轉為 RGB 顯示用

# 銳化卷積核,讓中心像素變得更「凸出」，也就是邊緣更清楚、圖更銳利。
#3x3 銳化濾波器 (Sharpening Kernel)
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
'''
| 區域      | 數值   | 功能              |
| ------- | ---- | --------------- |
| 中間（自己）  | `5`  | 保留、放大自己強度（加強本身） |
| 上、下、左、右 | `-1` | 減去鄰居的強度，抑制模糊    |
| 四角（0）   | `0`  | 不處理對角線像素        |

'''
# 用 OpenCV 卷積處理（自動處理三通道）
sharpened = cv2.filter2D(img, -1, kernel)
sharpened_rgb = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)

# 顯示結果
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Sharpened")
plt.imshow(sharpened_rgb)
plt.axis('off')

plt.tight_layout()
plt.waitforbuttonpress() # 等待按下任何鍵或滑鼠點擊


'''
卷積（Convolution）是將影像中的每個像素，根據它周圍像素與一個 卷積核（filter/kernel）
 的加權運算，來得到新值。

這個卷積核的數值不同，影像的效果就會不同：
| 卷積核                     | 功能效果    |
| ----------------------- | -------      |
| 平均濾波 (全部是正數，平均)         | 模糊      |
| 高斯核（中間大、邊緣小）            | 模糊、平滑   |
| 銳化（中心大，周圍為負）            | 加強邊緣、對比 |
| 邊緣偵測（如 Sobel、Laplacian） | 抓輪廓     |

'''
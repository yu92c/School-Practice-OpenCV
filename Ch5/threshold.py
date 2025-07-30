import cv2 as cv
import matplotlib.pyplot as plt

# 1. 載入彩色圖片並顯示
img = cv.imread('pic/detail.png')


# 2. 轉成灰階圖
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 3. 簡單閾值二值化（正向）
_, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# 4. 簡單閾值二值化（反向）
_, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

# 5. 自適應閾值（高斯方法）
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, 
    cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv.THRESH_BINARY_INV, 
    11, 9
)

# 6. 使用 matplotlib 顯示成一排
images = [img, gray, thresh, thresh_inv, adaptive_thresh]
titles = ['Original (BGR)', 'Gray', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'Adaptive (Gaussian)']

plt.figure(figsize=(15, 4))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))  # 彩色圖轉換為 RGB
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.waitforbuttonpress()  # 按任意鍵關閉

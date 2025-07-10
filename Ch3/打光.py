import cv2
import numpy as np
# 讓圖片中央變亮，邊緣變暗，就像有個手電筒照在圖片上。 ＃一次處理整張圖

# 讀入灰階圖片
img = cv2.imread('pic/xx.jpg', 0) # 0 表示轉成灰階（只有一個通道）

h, w = img.shape # 灰階（shape = (h, w)） # 彩色（shape = (h, w, 3)）

#| flag 數值 | 含義                                       |
#| ------- | ------------------------------------------ |
#| `-1`    | 保留原圖格式（包括透明通道）→ 可能是彩色，也可能是灰階，也可能是 4 通道 PNG |
#| `0`     | 強制以灰階讀入（單通道）                               |
#| `1`     | 強制以彩色讀入（忽略透明度）                            |



# 打光中心 & 範圍
x0, y0 = h // 2, w // 2   # 中央
sigma = 500

# 建立光照圖（高斯分布）
illum = np.zeros((h, w), dtype=np.float32)
for x in range(h):
    for y in range(w):
        illum[x, y] = np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

# 套用光照效果
img_lighted = (img.astype(np.float32) * illum)
img_lighted = np.clip(img_lighted, 0, 255).astype(np.uint8)

# 顯示
cv2.imshow('Original', img)
cv2.imshow('Lighted Image', img_lighted)
cv2.waitKey(0)


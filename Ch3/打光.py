import cv2 # OpenCV：用來讀取、處理、顯示圖片。
import numpy as np #數值運算工具：用來建立與處理像素陣列（例如浮點陣列）。

# 整體目標說明：模擬一張圖片上有光源照射，產生中央亮、四周暗的打光效果（Spotlight）。

# 讀灰階圖片
# img = cv2.imread('pic/xx.jpg', 0) # 0 表示轉成灰階（只有一個通道）

# 讀彩色圖片
img = cv2.imread('pic/cb.jpg', 1) 
#------------------------------------------------------------------------------

# h, w = img.shape # 灰階（shape = (h, w)） ,2D：只有亮度資訊
h,w,c = img.shape # 彩色（shape = (h, w, 3)）, 3D：每個 pixel 有 [B, G, R]

#| flag 數值 | 含義                                       |
#| ------- | ------------------------------------------ |
#| `-1`    | 保留原圖格式（包括透明通道）→ 可能是彩色，也可能是灰階，也可能是 4 通道 PNG |
#| `0`     | 強制以灰階讀入（單通道）                               |
#| `1`     | 強制以彩色讀入（忽略透明度）                            |


# 打光中心 & 範圍
x0, y0 = h // 2, w // 2   # 打光的中心點為圖片的正中央 。
                          # x0 是垂直方向中間（行）。 
                          # y0 是水平方向中間（列）。

sigma = 100 # 圓形 spotlight（中央亮、四周均勻漸暗）

# 控制光圈大小（擴散程度）  
# 數值越大 → 打光越廣、邊緣越柔和 。
#------------------------------------------------------------------------------

# 橢圓形 spotlight , 可以控制橢圓的「寬」與「高」。
# a = 300  # 垂直方向（y 軸）擴散 
# b = 100  # 水平方向（x 軸）擴散



# 建立光照圖（高斯分布）
# 光照圖（illumination map）
illum = np.zeros((h, w), dtype=np.float32)
for x in range(h):
    for y in range(w):
        # 圓形:
         illum[x, y] = np.exp(-((x - x0)**2 + (y - y0)**2) / (2 * sigma**2))

        # 橢圓形:
        # illum[x, y] = np.exp(-(((x - x0)**2)/a**2 + ((y - y0)**2)/b**2))

#------------------------------------------------------------------------------
# 套用光照效果：
# 灰色圖片
# img_lighted = (img.astype(np.float32) * illum)

# 彩色圖片
illum_3ch = np.repeat(illum[:, :, np.newaxis], 3, axis=2)  # 擴充為 3 通道
img_lighted = img.astype(np.float32) * illum_3ch           # 每個通道都乘光
#------------------------------------------------------------------------------

img_lighted = np.clip(img_lighted, 0, 255).astype(np.uint8)

# 顯示
cv2.imshow('Original', img)
cv2.imshow('Lighted Image', img_lighted)
cv2.waitKey(0)


# 仿射轉換（Affine Transformations）
# Shear 偏移 。
# 沿著 X 或 Y 軸「傾斜拉扯」，角度不變，長度不變 。
# 四邊形傾斜成平行四邊形，像被橡皮筋拉了一樣 。
# 不改物體內部角度，只改外框傾斜 。

# 原始正方形（未變形）：
#   +-----+
#   |     |
#   |     |
#   +-----+


#  Shear X（負數）,（向右傾）： 
#  +---------+
#  \  ABCDE  \
#   \  ABCDE  \
#    \  ABCDE  \
#     +---------+

# Shear X（正數）, （向左傾）：
#      +---------+
#     /  ABCDE  /
#    /  ABCDE  /
#   /  ABCDE  /
#  +---------+



import cv2
import numpy as np

# 讀取圖像
img = cv2.imread('pic/cb.jpg')
h, w = img.shape[:2] #只取高、寬（不含色彩通道）


# ===== 水平切變（Shear X） =====
shear_x = -0.5 # 正數 向左, 負數 向右。

# 平移補償：讓圖像在畫布中央對齊
lr = - shear_x * h / 2  # ❗ 負號，表示向左平移

# === 仿射矩陣 M_x ===
M_x = np.float32([
    [1, shear_x, lr],  # x' = x + shear_x * y + lr
    [0, 1,        0]   # y 不變
])

# === 輸出畫布寬度要加大，以容納傾斜後的圖像 ===
out_w = int(w + abs(shear_x) * h)
sheared_x = cv2.warpAffine(img, M_x, (out_w, h))

# === 顯示結果 ===
cv2.imshow('Original', img)
cv2.imshow('Shear X（向右傾斜）', sheared_x)
cv2.waitKey(0)
# Perspective Transformation
# 使用函式： cv2.getPerspectiveTransform() + cv2.warpPerspective()

# 效果比較：
# 拍到一張歪掉的白板（像梯形）
# crop：只能擷取歪掉的區域，但歪的還是歪的
# 透視轉換：會把這個梯形「拉正」成矩形，像你站在正前方看一樣

import cv2
import numpy as np

img = cv2.imread("pic/shop.png")  # 換成你的圖片路徑
print(img.shape)  

# 原圖上的四個角點
src_pts = np.float32([
    [320, 70],    # 左上
    [540, 60],    # 右上
    [250, 580],   # 左下
    [600, 590]    # 右下
])

# === 直接設定目標矩形大小（固定值）===
target_width = 300
target_height = 500

dst_pts = np.float32([
    [0, 0],                         # 左上
    [target_width - 1, 0],          # 右上
    [0, target_height - 1],         # 左下
    [target_width - 1, target_height - 1]  # 右下
])

# === 執行透視轉換 ===
M = cv2.getPerspectiveTransform(src_pts, dst_pts)
output = cv2.warpPerspective(img, M, (target_width, target_height))

# === 顯示結果 ===
cv2.imshow("Original", img)
cv2.imshow("Perspective Transform", output)
cv2.waitKey(0)
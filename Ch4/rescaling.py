import cv2
import numpy as np

img = cv2.imread('pic/c.png', -1)

h, w = img.shape[:2] #原圖的高度與寬度
new_h, new_w = h // 4, w // 4 #縮小後的高度與寬度，設為原來的 1/4

## 最近鄰插值
img_nearest = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_NEAREST)
img_nearest = cv2.resize(img_nearest, (w, h), interpolation=cv2.INTER_NEAREST)

# 雙線性插值
img_linear = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
img_linear = cv2.resize(img_linear, (w, h), interpolation=cv2.INTER_LINEAR)

# 雙立方插值
img_cubic = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
img_cubic = cv2.resize(img_cubic, (w, h), interpolation=cv2.INTER_CUBIC)

# 顯示視窗
cv2.imshow("Original Image", img)
cv2.imshow("Nearest Neighbor", img_nearest)
cv2.imshow("Bilinear", img_linear)
cv2.imshow("Bicubic", img_cubic)
cv2.waitKey(0)
cv2.destroyAllWindows()

#| 插值方式                 | 圖片特徵 & 差異                     |
#| -------------------- | ----------------------------- |
#| **Nearest Neighbor** | 顯著鋸齒狀邊緣，像素塊感強，細節糊掉但輪廓粗獷       |
#| **Bilinear**         | 邊緣柔化、像素平滑化，略模糊但自然，較柔順         |
#| **Bicubic**          | 平滑度最佳，最接近「模糊又自然」的效果，像小雞毛邊緣也更順 |

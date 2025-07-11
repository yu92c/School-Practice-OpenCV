# 雙立方內插法（Bicubic Interpolation）
# 透過考慮影像中 周圍 4×4 個像素（共 16 個像素） 來估算新的像素值。固定用 16 個點

#       y-axis ↑
#              |
#          ┌───────┐
#          │16格區域│ ← 參考區（4x4）
#          └───────┘
#              |
#             x-axis →
# 針對這些像素值進行數學運算（立方插值），計算出最適合的「中間值」。

import cv2
import numpy as np

def cubic_kernel(x):
    a = -0.5  #雙立方內插預設使用的就是 a = -0.5。

#| a 值   | 名稱（常見設定）               | 效果描述                   |
#| ------- | ---------------------- | ---------------------- |
#| -0.5  | **Catmull-Rom spline** | 最常用，畫質平滑不模糊，銳利適中，無過多波動 |
#| -0.75 | B-spline variant       | 更平滑、柔和（但可能過度模糊）        |
#| -1.0  | Cubic B-spline         | 模糊感明顯，用於特殊平滑處理         

    x = abs(x)
    if x <= 1:
        return (a + 2) * x**3 - (a + 3) * x**2 + 1
    elif x < 2:
        return a * x**3 - 5*a * x**2 + 8*a * x - 4*a
    else:
        return 0

# 主內插函數
def bicubic_resize(image, scale):
    h, w, c = image.shape
    new_h, new_w = int(h * scale), int(w * scale)

    build = np.zeros((new_h, new_w, c), dtype=np.uint8)

    for y_new in range(new_h):
        for x_new in range(new_w):
            x = x_new / scale
            y = y_new / scale
            x0 = int(np.floor(x))
            y0 = int(np.floor(y))

            for ch in range(c):
                value = 0.0
                total_weight = 0.0

                for m in range(-1, 3):
                    for n in range(-1, 3):
                        xm = min(max(x0 + n, 0), w - 1)
                        ym = min(max(y0 + m, 0), h - 1)
                        dx = x - (x0 + n)
                        dy = y - (y0 + m)

                        wx = cubic_kernel(dx)
                        wy = cubic_kernel(dy)
                        weight = wx * wy

                        value += weight * image[ym, xm, ch]
                        total_weight += weight

                build[y_new, x_new, ch] = np.clip(value / total_weight, 0, 255)

    return build


img = cv2.imread("pic/c.png", -1)
enlarged = bicubic_resize(img, scale=4)
cv2.imshow("Bicubic Result", enlarged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#什麼時候適合用雙立方內插？
#希望圖片「放大但畫質不變差」
#對畫質要求高（印刷、展示用圖）
#圖片邊緣多（建築、漫畫、插畫等）

#| 特性            | 說明                                |
#| -------------- | ----------------------------------- |
#| *畫質最平滑**   | 因為使用 16 個周圍像素進行插值，畫面比「最近鄰」與「雙線性」更細緻 
#| *保留細節最好**  | 特別是邊緣細節與漸層過渡自然，抗鋸齒效果佳               
#| *運算最複雜**   | 每個像素都要計算立方函數，速度比其他方法慢很多             
#| *適合高品質放大** | 例如：人像、風景圖、插畫等希望畫質提升但不要鋸齒或馬賽克的用途     

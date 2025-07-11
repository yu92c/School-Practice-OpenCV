#| 內插法                    | 原理                    | 畫質特性              | 運算速度       |
#| ---------------------- | ------------------------- | -------------------- | ------------- |
#| 最近鄰 (Nearest Neighbor) | 直接取最靠近的像素值        | 鋸齒感強、不平滑       | ✅ 非常快（最快）|
#| 雙線性 (Bilinear)         | 根據 4 個鄰近點線性加權平均  | 平滑、柔和，但有點模糊  | ⚠️ 中等        |
#| 雙立方 (Bicubic)          | 根據 16 個鄰點進行三次方插值 | 最平滑、保留細節最多    | ❌ 最慢        |

# Nearest Neighbor:
# cv2.resize(img, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)

import cv2
import numpy as np
                                            # scale 是「縮放比例」
def nearest_neighbor_upscale(img, scale=15): #放大倍數（預設放大 2 倍）。
    h, w = img.shape[:2]
    new_h, new_w = h * scale, w * scale #計算放大後的尺寸。
    result = np.zeros((new_h, new_w, img.shape[2]), dtype=np.uint8)
                                    #img.shape[2] 就是這個 tuple 的第 3 個數字，也就是通道數。
    for y in range(new_h):
        for x in range(new_w):

            # 找出對應原圖的位置（用最近鄰：四捨五入 or 向下取整）
            # 最近鄰內插法：在新圖 (x, y) 的點，回推原圖對應的最近座標。
            # 這裡使用「整數除法」：找出原圖中的位置 (src_x, src_y)。
            src_x = x // scale
            src_y = y // scale

            # 將原圖中 (src_y, src_x) 的像素值，複製貼到新圖 (y, x) 上。
            result[y, x] = img[src_y, src_x]

    return result

def main():
    img = cv2.imread("pic/c.png", -1)
    print(img.shape) 
    enlarged = nearest_neighbor_upscale(img, scale=15) # enlarged 放大後的版本
    print(enlarged.shape) 

    cv2.imshow("Original", img)
    cv2.imshow("Nearest Neighbor Upscale", enlarged)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()


# 與 cv2.resize() 比較方式:
# resized = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
# 跟上面的效果一樣，只是速度更快。

#最近鄰插值的典型效果特徵：
#| 特徵           | 圖片中的表現                       |
#| ------------- | --------------------------------- |
#| **鋸齒感／格子狀邊緣** | 小雞輪廓的邊緣有明顯「鋸齒感」，像是一格一格貼出來的        
#| **放大但不模糊**      | 顏色區塊是「複製」原圖像素來填滿，沒有模糊或混色          
#| **色塊感明顯**        | 每一筆線條、眼睛、嘴巴、雞冠，都是由「原圖一個像素」放大形成的方塊 
#| **清晰但粗糙**        | 放大後輪廓明顯，不柔和，呈現像素風格感               

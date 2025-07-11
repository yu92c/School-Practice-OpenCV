# 把原圖像素放大兩倍並「疏疏地」填進新圖， 每個方向都放大 2 倍：寬 ×2，高 ×2 。
# 但畫面只有 1/4 像素有值，其餘是黑色空洞。

# 原圖像素格：
# A B
# C D


# forward mapping 的結果會變成這樣（只標記有填值的格子）：
# A _ B _
# _ _ _ _
# C _ D _
# _ _ _ _


import cv2
import numpy as np

def forward_mapping(f):
    h, w = f.shape[:2]  # 取得圖片的「高度（rows）」與「寬度（columns）」。

    g = np.zeros([h*2, w*2, 3], dtype='uint8')  
    # 建立一個大小為原圖 2 倍 的空白圖片 g
    # 將原來影像的高度與寬度各乘以 2。
    # 3：表示 RGB 三個通道。
    # dtype='uint8'：使用 8 位元無符號整數（0~255）來儲存像素值。

    # 對原圖每一個像素進行 forward mapping
    for x in range(h):
        for y in range(w):
            for k in range(3):
                g[x*2, y*2, k] = f[x, y, k]
                # 把原圖 (x, y) 的第 k 個通道的像素值，放到新圖 (x*2, y*2) 的對應位置。
                # 效果是圖像放大 2 倍，但只有 1/4 像素有值，其他是黑的（0），因為沒進行補值。

    return g

def main():
    img1 = cv2.imread('pic/house.png', -1)  # -1 表示保留圖像原始格式（不轉灰階、不去 alpha channel）。
    print(img1.shape)  # 原圖(680, 828, 4)
    img2 = forward_mapping(img1)
    print(img2.shape)  # after forwardind (1360, 1656, 3)

    cv2.imshow("Original Image", img1)
    cv2.imshow("Forward Mapping", img2)
    cv2.waitKey(0)

main()


#| 倍數     | 結果畫面                           | 感覺是                 |
#| ------ | ------------------------------ | ------------------------- |
#| `×2`   | 有規律、間距一致、容易觀察結構                | 視覺效果穩定、常用教學           |
#| `×3`   | 更稀疏，畫面內容更小                     | 點太分散，不補值會很空              |
#| `×1.5` | 無法直接對應 pixel，需補插值（不適合 forward） | 通常用在 **backward mapping** |

#因為 forward mapping 是從原圖「推像素」出去：
#若 N 是奇數，如 3：
#每個像素距離更大，畫面更稀疏。 圖片看起來反而「縮小」。

#若 N 是偶數（如 2, 4）：
#排列整齊、每個格子是規律的正方形，比較好看出效果。
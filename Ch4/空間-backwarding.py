# backwarding 強調的是「從新圖像素回原圖取值的做法」。
# backward mapping 放大影像，沒有黑點、畫面完整。
# 放大影像，沒有黑點、畫面完整， 圖片的「像素數量」變成原本的 4 倍。
# 這是空間變大、細節變稀疏填滿，但不是產生新細節。

import cv2
import numpy as np

def backward_mapping(f):
    h, w = f.shape[:2]
    g = np.zeros([h*2, w*2, 3], dtype='uint8')

    for x in range(h*2):
        for y in range(w*2):
          
            s_h = x // 2 #在原圖中，對應的 x 座標
            s_w = y // 2 ##在原圖中，對應的 y 座標

            for k in range(3):  # RGB通道
             g[x, y, k] = f[s_h, s_w, k] #從原圖取的像素
             # g[x, y] 新圖的位置，準備填入取到的值     
    return g

def main():
    img1 = cv2.imread("pic/house.png", -1)
    print("Original image size:", img1.shape)

    img2 = backward_mapping(img1)
    print("Backward mapped image size:", img2.shape)

    cv2.imshow("Original Image", img1)
    cv2.imshow("Backward Mapping", img2)
    cv2.waitKey(0)


main()
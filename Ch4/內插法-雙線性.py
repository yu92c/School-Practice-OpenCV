#雙線性插值 (Bilinear Interpolation)
import cv2
import numpy as np

def bilinear_upscale(img, scale=9):
    h, w = img.shape[:2]
    new_h, new_w = h * scale, w * scale

    result = np.zeros((new_h, new_w, img.shape[2]), dtype=np.uint8)

    for y in range(new_h):
        for x in range(new_w):
            # 對應到原圖的浮點座標（非整數）
            src_x = x / scale
            src_y = y / scale

            # 取上下左右整數座標
            x0 = int(np.floor(src_x))
            x1 = min(x0 + 1, w - 1)
            y0 = int(np.floor(src_y))
            y1 = min(y0 + 1, h - 1)

            # 權重
            dx = src_x - x0
            dy = src_y - y0

            # 對每個通道進行雙線性內插
            for c in range(img.shape[2]):
                value = (
                    (1 - dx) * (1 - dy) * img[y0, x0, c] +
                    dx * (1 - dy) * img[y0, x1, c] +
                    (1 - dx) * dy * img[y1, x0, c] +
                    dx * dy * img[y1, x1, c]
                )
                result[y, x, c] = int(value)

    return result

def main():
    img = cv2.imread("pic/c.png", -1)
    print("Original:", img.shape)

    enlarged = bilinear_upscale(img, scale=9)
    print("Bilinear enlarged:", enlarged.shape)

    cv2.imshow("Original", img)
    cv2.imshow("Bilinear Upscale", enlarged)
    cv2.waitKey(0)

main()


#| 特徵        | 圖中觀察說明                                |
#| ---------- | ----------------------------------------- |
#| 邊緣變平滑    | 雞的外框黑線變得不再是鋸齒狀，而是有一點柔和過渡，不像最近鄰那樣一格一格的     
#| 顏色過渡自然   | 像翅膀上的線條與黃色填色之間有「模糊融合感」，不像最近鄰那樣明確切開        
#| 細節有點模糊  | 紅色雞冠、眼睛的邊緣、腳的線條略微變模糊，這是雙線性加權平均的副作用        
#| 沒有馬賽克方格感 | 放大後看不到「像素方塊」的格狀結構，這代表不是最近鄰法，而是雙線性或更進階的內插法 

import cv2
import numpy as np

def image_quantization(f, bits):
                        # bits: 量化成的位元數（例如 5 位元 → 2⁵ = 32 階灰階）
    g = f.copy()
    #建立 g 作為輸出圖像，並複製原始影像 f。 

    nr, nc = f.shape[:2]
    #取得輸入影像的高（nr）與寬（nc）。

    levels = 2 ** bits
    #計算總共要分幾個灰階階層

    interval = 256 / levels
    #間隙
    #將 0~255 的像素值區間平均分割為 levels 段，每段的大小（像素範圍）是 interval。

    gray_level_interval = 255 / (levels - 1)

    for k in range(256):
     for l in range(levels):
        if k >= l * interval and k < (l + 1) * interval:
                table[k] = round(l * gray_level_interval)

#建立查找表：
#對於每個像素值 k（0~255），找出它屬於哪個區間 l
#並把它對應成新的值（量化後的灰階）
#用 round() 取整數，是為了符合像素格式（整數）

    for x in range(nr):
        for y in range(nc):
            g[x, y] = np.uint8(table[f[x, y]])
#用查表法，將每個像素原始值 f[x, y] 對應查找表，得到量化後的值。
#存到 g[x, y] 中。

    return g

def main():
    img1 = cv2.imread('pic/mm.jpg', -1)
    img2 = image_quantization(img1, 5) #對原圖 img1 進行 5 位元量化（變成 32 階灰階）。

    cv2.imshow("Original Image", img1)
    cv2.imshow("Quantization", img2)
    cv2.waitKey(0)



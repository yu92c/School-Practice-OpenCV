import cv2
import numpy as np

# 彩色量化是控制「色彩豐富度」。
# RGB 彩色量化 → 就能看見「顏色變少、變粗糙」的明顯視覺變化。



def image_quantization_color(f, bits):
    g = f.copy()
    h, w, c = f.shape  # c=3（彩色圖三通道）

    levels = 2 ** bits
    interval = 256 / levels
    gray_level_interval = 255 / (levels - 1)

    # 建立查找表
    table = np.zeros(256)
    for k in range(256):
        for l in range(levels):
            if k >= l * interval and k < (l + 1) * interval:
                table[k] = round(l * gray_level_interval)

    # 每個通道都要各別量化
    for ch in range(3):  # BGR 三通道
        for x in range(h):
            for y in range(w):
                g[x, y, ch] = np.uint8(table[f[x, y, ch]])

    return g

def main():
    img1 = cv2.imread('pic/cc.jpg', 1)  # 用「1」載入彩色圖

    img2 = image_quantization_color(img1, 1)  
    #最多 就是 8（原圖），再高也沒意義，因為影像檔本身最多就是 8 位元每通道。

    #| 設定值 | 每通道階數 | 總顏色數量                     |
    #| --- | ----- | ------------------------- |
    #| `8` | 256   | 256 × 256 × 256 ≈ 1670 萬色 | --> 不會改變
    #| `7` | 128   | 128 × 128 × 128 ≈ 209 萬色  |
    #| `4` | 16    | 16 × 16 × 16 = 4096 色     |
    #| `3` | 8     | 512 色                     |
    #| `2` | 4     | 64 色                      |
    #| `1` | 2     | 8 色（原始紅綠藍 + 黑白灰）          |


    cv2.imshow("Original Color", img1)
    cv2.imshow("Quantized Color", img2)
    cv2.waitKey(0)

main()

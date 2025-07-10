import cv2
import numpy as np

#量化 = 降低精度、簡化細節
#適合用於：
#儲存壓縮
#特徵萃取前處理
#應用在嵌入式系統（記憶體很小）
#視覺風格化（如像素風）

def image_quantization(f, bits):
                        # bits: 量化成的位元數（例如 5 位元 → 2⁵ = 32 階灰階）
    g = f.copy()
    #建立 g 作為輸出圖像，並複製原始影像 f。 

    h, w = f.shape[:2] 
    #a = [10, 20, 30, 40, 50]
    #print(a[:2])  # [10, 20] 取前面兩個值


    levels = 2 ** bits
    #＊＊次方
    
    interval = 256 / levels
    #間隙
    #將 0~255 的像素值區間平均分割為 levels 段，每段的大小（像素範圍）是 interval。

    gray_level_interval = 255 / (levels - 1)

    #bits = 2
    #levels = 2 ** bits = 4
    # 255 / (4 - 1) = 85
    #| 等級 `l` | 灰階值公式 `l × gray_level_interval` | 結果 |
    #| ------ | -------------------------------------| --- |
    #| 0      | 0 × 85                               | 0   |
    #| 1      | 1 × 85                               | 85  |
    #| 2      | 2 × 85                               | 170 |
    #| 3      | 3 × 85                               | 255 |


    table = np.zeros(256)  

    for k in range(256):
     for l in range(levels):
        if k >= l * interval and k < (l + 1) * interval:
                table[k] = round(l * gray_level_interval)

#建立查找表：
#對於每個像素值 k（0~255），找出它屬於哪個區間 l
#並把它對應成新的值（量化後的灰階）
#用 round() 取整數，是為了符合像素格式（整數）

    for x in range(h):
        for y in range(w):
            g[x, y] = np.uint8(table[f[x, y]])
#用查表法，將每個像素原始值 f[x, y] 對應查找表，得到量化後的值。
#存到 g[x, y] 中。

    return g

def main():  #「定義」函式，不會自動執行
    img1 = cv2.imread('pic/xx.jpg', -1)
    img2 = image_quantization(img1, 2) 
    #| 位元數 | 灰階層數（levels） | 效果     |
    #| --- | ------------ | ------------- |
    #| 8   | 256          | 幾乎無損（原圖）         |
    #| 5   | 32           | 有一點變化              |
    #| 4   | 16           | 可明顯看到灰階層化        |
    #| 2   | 4            | 幾乎只有黑、白與幾個中間色 |
    #| 1   | 2            | 只有黑與白（二值圖）      |


    cv2.imshow("Original Image", img1)
    cv2.imshow("Quantization", img2)
    cv2.waitKey(0)

main()
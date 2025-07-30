import numpy as np
import cv2
import scipy.special as special
import matplotlib.pyplot as plt 

def beta_correction(f, a=2.0, b=2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x) * 255, 0)

    if f.ndim != 3:  # 灰階
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:  # 彩色
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]
    return g

def main():
    # 讀取灰階圖
    img0 = cv2.imread('pic/food.png', 0-1)
   
    # 做 Beta 校正
    img1 = beta_correction(img0, a=0.5, b=0.5)
    #Beta 函數的形狀會變成 中間低、兩邊高（類似「U型分佈」）。
    #所以暗部與亮部的對比都被拉大，中間灰度會被壓縮。
    #效果：整體影像偏向兩端，導致中間灰階少，所以 整體「偏暗」或「過曝」感。


    img2 = beta_correction(img0, a=2.0, b=2.0)
    #Beta 函數呈現「中間高、兩邊低」（像山丘）。
    #暗部與亮部會被壓縮，中間灰度被提升。
    #效果：「顏色變濃」、「細節變清晰」。


    # 建立拼圖顯示
    images = [img0, img1, img2]
    titles = ["Original", "Beta (a=b=0.5)", "Beta (a=b=2.0)"]

    plt.figure(figsize=(12, 4))
    for i in range(3):
        plt.subplot(1,  3, i + 1)
        if len(images[i].shape) == 2:
            plt.imshow(images[i], cmap='gray')  # 灰階圖
        else:
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # 彩色圖轉 RGB
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.waitforbuttonpress()  # 按任意鍵關閉

main()

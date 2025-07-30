import numpy as np
import cv2
import matplotlib.pyplot as plt

def image_negative(f):
    g = 255 - f
    return g

def main():
    img1 = cv2.imread('pic/rbg.png', -1)
    img2 = image_negative(img1)
   

    # -------- 額外用於 plt 顯示 --------
    images = [img1, img2]
    titles = ['Original', 'Image Negative']

    # ---------- 顯示 1x2 拼圖 ----------
    plt.figure(figsize=(10, 5))  # 設定畫布大小

    for i in range(len(images)):
        plt.subplot(1, 2, i+1)  # 建立 1 行 2 列的圖排版
        if len(images[i].shape) == 2:  # 如果是灰階圖
            plt.imshow(images[i], cmap='gray')
        else:  # 彩色圖
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))

        plt.title(titles[i])
        plt.axis('off')  # 關閉座標軸顯示

    plt.tight_layout()  # 自動調整排版避免重疊
    plt.waitforbuttonpress()  # 等待任意鍵關閉

main()

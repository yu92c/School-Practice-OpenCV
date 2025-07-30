# 伽瑪校正 Gamma Correction
# 簡單有效的「整體亮度非線性調整」

'''
| γ 值   | 說明                 | 對圖像效果         |
|--------|----------------------|--------------------|
| γ < 1  | 提升暗部亮度（變亮）   | 暗區細節變清楚     |
| γ = 1  | 無改變（恆等轉換）     | 不變               |
| γ > 1  | 壓抑亮部（變暗）       | 高光細節被保留     |
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

def gamma_correction(f, gamma=2.0):
    """
    執行 Gamma 校正：
    - f: 原始影像（灰階或彩色）
    - gamma: γ 值（非線性調整指數）
    """
    g = f.copy()
    nr, nc = f.shape[:2]
    c = 255.0 / (255.0 ** gamma)  # Normalization factor
    table = np.array([round((i ** gamma) * c, 0) for i in range(256)])

    # 灰階影像處理
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:
        # 彩色影像處理
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]

    return g

def main():
    img = cv2.imread('pic/flower2.png')  # 原圖（彩色或灰階皆可）
    if img is None:
        print("⚠️ 找不到圖片，請確認檔案路徑是否正確！")
        return

    # 執行不同 gamma 值的校正
    img1 = gamma_correction(img, 0.1) #γ = 0.1：極度提亮,暗部區域幾乎變成白色。
    								#整體畫面非常亮，對比度會下降。
    img2 = gamma_correction(img, 0.2)
    img3 = gamma_correction(img, 8) # > 1 變暗,壓暗過亮的區域、保留高光細節


    # ---------- 使用 matplotlib 合併顯示 ----------
    images = [img, img1, img2, img3]
    titles = ["Original", "Gamma = 0.1", "Gamma = 0.2", "Gamma = 8"]

    plt.figure(figsize=(12, 4))
    for i in range(4):
        plt.subplot(1, 4, i + 1)
        if len(images[i].shape) == 2:
            plt.imshow(images[i], cmap='gray')  # 灰階圖
        else:
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # 彩色圖轉 RGB
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.waitforbuttonpress() # 等待按下任何鍵或滑鼠點擊


main()

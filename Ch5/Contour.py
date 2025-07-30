import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# ---------- 處理圖像 ----------
img = cv.imread('pic/eyes.png', -1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img, (19, 19), cv.BORDER_DEFAULT)
canny = cv.Canny(img, 125, 175)
blank = np.zeros_like(img)
contours, _ = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (255, 0, 0), 1)

#GaussianBlur 是一種低通濾波器，它平滑影像、消除雜訊。
#ksize=(19, 19) 表示非常大的模糊範圍，會讓影像邊緣變得非常柔和。
#結果：
#Canny 邊緣檢測找不到明顯的變化（白線變少）
#輪廓（Contours）也因此少了很多或變得不清楚

# ---------- 圖片與標題配對 ----------
images = [img, gray, blur, canny, blank]
titles = ["Original", "Gray", "Blur", "Canny", "Contours"]

# ---------- 顯示 2x3 拼圖 ----------
plt.figure(figsize=(10, 6)) #建立一個新的圖形視窗（Figure）
                            #指整個畫布寬度為 10 英吋、高度為 6 英吋
                            #會影響圖像與圖像間的空白比例（越大，空白越多）
for i in range(len(images)):
    plt.subplot(2, 3, i+1) #將整個畫布分成 2 行 3 欄（共 6 個區域）
                           #i+1 表示現在要繪製的是第幾個子圖（subplot）
                           #例如：第一張圖會放在第 1 格、第二張圖放在第 2 格⋯⋯
    # 判斷是否為灰階圖，用 cmap=gray 顯示
    if len(images[i].shape) == 2: #判斷當前圖片是否為「灰階圖」
                                  #灰階圖只有高和寬（沒有色彩通道），所以 shape 長度會是 2
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
    
    plt.title(titles[i])
    plt.axis('on') # off為關閉每張圖的座標軸（x, y 軸不顯示）

# 關鍵調整間距
plt.subplots_adjust(wspace=0.05, hspace=0.1)  #數值越小 → 間距越小，圖像越緊密
plt.show()

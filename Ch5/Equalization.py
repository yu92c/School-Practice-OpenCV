import cv2 as cv
import matplotlib.pyplot as plt

#直方圖均衡化函式，用來提升影像的對比度。
#但僅適用於 單通道（gray-scale）影像。
'''
什麼情況適合用 Histogram Equalization？
醫療影像（如 X 光）

晚上或低光環境下拍攝的圖

灰階圖太平淡，看不到細節
'''

img = cv.imread('pic/dark.png', 0)  # 灰階
equalized = cv.equalizeHist(img) # cv.equalizeHist() 只能處理單通道的 灰階影像。


# ---------- 圖片與標題配對 ----------
images = [img, equalized]
titles = ["Original", "Equalized"]

# ---------- 顯示 2x2 拼圖 ----------
plt.figure(figsize=(12, 10)) #建立一個新的圖形視窗（Figure）
                            #指整個畫布寬度為 10 英吋、高度為 6 英吋
                            #會影響圖像與圖像間的空白比例（越大，空白越多）
for i in range(len(images)):
    plt.subplot(2, 2, i+1) 
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
plt.waitforbuttonpress() # 等待按下任何鍵或滑鼠點擊


import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram( f ): #傳入一張圖片 f，決定它是灰階或彩色後畫出直方圖。
	if f.ndim != 3: #判斷影像是灰階還是彩色
                    #如果影像維度不是 3（灰階圖通常是 2D），就走灰階流程。
					
        #灰階圖直方圖
		hist = cv2.calcHist( [f], [0], None, [256], [0,256] )#cv2.calcHist()：計算影像的直方圖
		plt.plot( hist )
	else:
		#彩色圖直方圖
		color = ( 'b', 'g', 'r' )
		for i, col in enumerate( color ):
			hist = cv2.calcHist( f, [i], None, [256], [0,256] )
			plt.plot( hist, color = col )
	plt.xlim( [0,256] )

 
def main():
    pass  # 原本 main() 留空，無更動

#----------------------------
# 🖼 額外合併顯示原圖 + 灰階直方圖 + 彩色直方圖
#----------------------------

# 讀取原圖與轉灰階
img = cv2.imread('pic/cb.jpg', -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 計算灰階直方圖
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# 計算彩色直方圖 (b, g, r)
colors = ('b', 'g', 'r')
color_hists = [cv2.calcHist([img], [i], None, [256], [0, 256]) for i in range(3)]

# 建立 1x3 的視窗布局
plt.figure(figsize=(15, 5))

# 原圖：左
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

# 灰階直方圖：中
plt.subplot(1, 3, 2)
plt.plot(gray_hist, color='black')
plt.title("Grayscale Histogram")
plt.xlabel("Intensity")
plt.ylabel("#Pixels")
plt.xlim([0, 256])

# 彩色直方圖：右
plt.subplot(1, 3, 3)
for hist, col in zip(color_hists, colors):
    plt.plot(hist, color=col)
plt.title("Color Histogram")
plt.xlabel("Intensity")
plt.ylabel("#Pixels")
plt.xlim([0, 256])

# 緊湊排版
plt.tight_layout()
plt.waitforbuttonpress() # 等待按下任何鍵或滑鼠點擊

'''
x=255 的位置有個超高的峰值
表示圖中有非常多幾乎是白色的像素
'''
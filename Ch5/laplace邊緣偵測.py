'''
Laplacian 和 Sobel 差異：
| 項目   | Sobel     | Laplacian     |
| ---- | --------- | ------------- |
| 邊緣類型 | 一階導數，方向性強 | 二階導數，**無方向性** |
| 偵測類型 | 可選 x/y 方向 | 同時偵測所有方向的邊緣   |
| 影像風格 | 線條感強烈     | 邊緣明亮，但比較模糊    |
| 效果   | 適合輪廓提取    | 適合「邊緣強度」的粗略檢測 |

'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

def laplacian( f ):
	temp = cv2.Laplacian( f, cv2.CV_32F ) 
	'''
	邊緣 → 亮白
    非邊緣 → 接近黑色 (0)
	'''
	g = np.uint8( np.clip( temp, 0, 255 ) )
	return g
		
def main():
    img1 = cv2.imread('pic/highway.png', -1)
    img2 = laplacian(img1)

    # 合併顯示
    images = [img1, img2]
    titles = ['Original', 'laplacian']

    plt.figure(figsize=(16, 4))  # 四張圖橫排
    for i in range(2):
        plt.subplot(1, 2, i + 1)
        if len(images[i].shape) == 3:
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # BGR → RGB
        else:
            plt.imshow(images[i], cmap='gray')  # 灰階圖用 gray colormap
        plt.title(titles[i])
        plt.axis('off')  # 關閉座標軸

    plt.tight_layout()
    plt.waitforbuttonpress()  # 等待任意鍵或滑鼠點擊

main()
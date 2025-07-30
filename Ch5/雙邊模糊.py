import numpy as np
import cv2
import matplotlib.pyplot as plt 

#雙邊模糊功能
'''
| 功能項目     | 說明                          |
| -------- | ------------------------------- |
| 去除雜訊   | 平滑圖像，減少顆粒感（graininess），常用於降噪處理。 |
| 保留邊緣細節 | **與一般模糊不同**，不會讓邊緣變模糊，能保持物體輪廓清晰。 |
| 適合處理人臉 | 能有效去除皮膚雜訊、光影不均，而不模糊眼睛、嘴巴等邊界區域。  |
| 可用於卡通化 | 作為「卡通濾鏡」前處理步驟，搭配邊緣偵測可製作卡通效果。    |

'''
img1 = cv2.imread('pic/face.png', -1)
print("影像資料型別 dtype:", img1.dtype)
print("影像形狀 shape:", img1.shape)
#img.shape 的意思 (H, W, C)：
'''
H = 566：高度（rows）

W = 640：寬度（columns）

C = 4：通道數（channels）
'''

#通道數對應說明：
'''
| shape\[-1] 值（通道數） | 類型     | 說明                      |
| ----------------- | ------   | ----------------------- |
| 1                 | 灰階圖    | 僅有亮度資訊（黑白）              |
| 3                 | 彩色圖    | BGR 三通道（藍、綠、紅）          |
| 4                 | 彩色 + A  | BGRA 四通道，多了 Alpha「透明通道」 |

'''


# 判斷通道數：若為 4 通道（BGRA），轉為 BGR（3 通道）
if img1.shape[2] == 4:
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGRA2BGR)

# 使用 bilateral filter（雙邊濾波）
img2 = cv2.bilateralFilter(img1.copy(), 15, 200, 200)
'''
| 模糊程度       | 建議設定                                        |
| ---------- | ------------------------------------------- |
| 輕微模糊（保細節）   | `d=5~9, sigmaColor=20~40, sigmaSpace=10~20` |
| 中等模糊           | `d=11, sigmaColor=50, sigmaSpace=50`        |
| 強烈模糊（磨皮效果） | `d=15~21, sigmaColor=100+, sigmaSpace=100+` |

'''


'''
cv2.bilateralFilter() 只支援以下格式的圖片：

CV_8UC1（灰階，shape: (H, W)）

CV_8UC3（BGR 彩色圖，shape: (H, W, 3)）
'''


## 使用 matplotlib 顯示原圖與濾波後的圖像
images = [img1, img2]
titles = ["Original", "Bilateral Filtering"]

plt.figure(figsize=(8, 4))  # 調整大小
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # BGR → RGB
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.waitforbuttonpress()  # 等待任意鍵或滑鼠點擊才關閉
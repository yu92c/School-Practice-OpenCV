import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'  # macOS 常見字型


def Sobel_gradient(f, direction=1):
    sobel_x = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    sobel_y = np.array([[-1,  0,  1],
                        [-2,  0,  2],
                        [-1,  0,  1]])
    if direction == 1:
        grad_x = cv2.filter2D(f, cv2.CV_32F, sobel_x)
        gx = abs(grad_x)
        g = np.uint8(np.clip(gx, 0, 255))
    elif direction == 2:
        grad_y = cv2.filter2D(f, cv2.CV_32F, sobel_y)
        gy = abs(grad_y)
        g = np.uint8(np.clip(gy, 0, 255))
    else:
        grad_x = cv2.filter2D(f, cv2.CV_32F, sobel_x)
        grad_y = cv2.filter2D(f, cv2.CV_32F, sobel_y)
        magnitude = abs(grad_x) + abs(grad_y)
        g = np.uint8(np.clip(magnitude, 0, 255))
    return g

# 主程式
img = cv2.imread('pic/highway.png')
gx = Sobel_gradient(img, 1)  # x 方向（垂直邊緣）
gy = Sobel_gradient(img, 2)  # y 方向（水平邊緣）
g = Sobel_gradient(img, 3)   # 綜合邊緣

'''
| 名稱        | Kernel 作用方向 | 偵測出什麼邊緣（形狀）     |
| --------- | ----------- | --------------- |
| `Sobel X` | 橫向卷積（左右梯度）  | **垂直邊緣**（直直站的線） |
| `Sobel Y` | 垂直卷積（上下梯度）  | **水平邊緣**（橫著的線）  |

'''


# 顯示圖像
plt.figure(figsize=(14, 4))

plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title("Sobel X 垂直邊緣")
plt.imshow(gx, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.title("Sobel Y 水平邊緣")
plt.imshow(gy, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.title('綜合邊緣')
plt.imshow(g, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.waitforbuttonpress()  # 等待任意鍵或滑鼠點擊才關閉



'''
用法:
| 想做的事情                       | 使用建議                           |
| ------------------             | ------------------------------ |
| 快速看亮度變化（邊緣大概在哪）      | `Sobel`                        |
| 想要乾淨又精準的邊緣              | `Canny`                        |
| 想擷取物體外框做分析（形狀、面積等） | `Canny → Threshold → Contours` |
'''


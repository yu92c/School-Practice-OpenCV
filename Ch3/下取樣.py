import cv2 as cv
import numpy as np


img = cv.imread('pic/rbg.png')
print("Original size:", img.shape)
cv.imshow('original', img)


# 降低解析度
def downsampling(f, rate):  # f：輸入圖像 # rate：下取樣倍率（例如 2 就是取一半解析度）
    nr, nc = f.shape[:2]
           # f.shape[:2]：取原始影像的高（rows）和寬（cols）

# nr、nc 是下取樣後的新高、新寬
# 用整數除法 //，保證不會出現小數

    g = np.zeros((nr // rate, nc // rate), dtype='uint8')

# 建立一個下取樣後的新圖像 g，初始值全是 0（黑色）
# 使用 uint8，表示像素範圍是 0~255（灰階影像）

    
    for x in range(nr // rate):
        for y in range(nc // rate):
            g[x, y] = f[x * rate, y * rate]


    return g


rate =  16 # 程度

# 指定要下取樣的通道（0=藍, 1=綠, 2=紅）
target_channel = 0   # 可以改 1 或 2 試試

# (一起看）顏色取樣
down = downsampling(img[:, :, target_channel], rate)
print("Downsampled size:", down.shape)
#  cv.imshow(f'downsampling x{rate} | channel {target_channel}', down)


# 模糊感：只要你有「下取樣 ➜ 再放大」就會模糊
up = cv.resize(down, (img.shape[1], img.shape[0]), interpolation=cv.INTER_LINEAR)
cv.imshow(f'downsampling x{rate} | upsampled (模糊)', up)


# 三個顏色分開看 , 刻意只取了單一通道 來做取樣。 （灰階強度分析）
# cv.imshow('Blue channel (0)', img[:, :, 0])
# cv.imshow('Green channel (1)', img[:, :, 1])
# cv.imshow('Red channel (2)', img[:, :, 2])

cv.waitKey(0)


import cv2 as cv
import numpy as np

img = cv.imread('pic/rbg.png')
print("Original size:", img.shape)
cv.imshow('original', img)

# 彩色下取樣：每個通道都處理
def downsampling_color(f, rate):
    nr, nc = f.shape[:2]
    g = np.zeros((nr // rate, nc // rate, 3), dtype='uint8')  # 注意：3通道
    for ch in range(3):  # 對 BGR 每個通道都下取樣
        for x in range(nr // rate):
            for y in range(nc // rate):
                g[x, y, ch] = f[x * rate, y * rate, ch]
    return g

rate = 16

# 做彩色下取樣
down_color = downsampling_color(img, rate)
print("Downsampled size:", down_color.shape)

# 放大回原本大小（產生模糊效果）
up = cv.resize(down_color, (img.shape[1], img.shape[0]), interpolation=cv.INTER_LINEAR)
cv.imshow(f'downsampling x{rate} | 彩色模糊', up)

cv.waitKey(0)

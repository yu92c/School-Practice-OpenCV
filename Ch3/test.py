import numpy as np
import cv2

# 讀入圖片
img = cv.imread('pic/cb.jpg')
cv.imshow('original', img)

# 取得圖片尺寸
height, width = img.shape[:2]

# 建立旋轉矩陣，旋轉中心是圖片中心，旋轉角度30度，縮放比為1
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1.0)
'''
cv2.getRotationMatrix2D(center, angle, scale)說明

|參數       | 說明                                           
| -------- | -------------------------------------------- 
| `center` | 旋轉中心點 `(x, y)`，這邊是圖片中心 `(width/2, height/2)` 
| `angle`  | 旋轉角度（單位：度）<br>正值為**逆時針旋轉**，負值為**順時針旋轉**      
| `scale`  | 縮放比例，`1.0` 表示原尺寸不縮放                          



'''

# 套用仿射轉換（即影像旋轉）
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

'''
cv2.warpAffine(src, M, dsize)

| 參數     | 說明                                     
| ------- | -------------------------------------- 
| `src`   | 原始圖片（例如 `img`）                         
| `M`     | 仿射轉換矩陣（這裡是 `rotation_matrix`）          
| `dsize` | 輸出圖像的大小（這裡是 `(width, height)`，表示保持原尺寸） 


'''

# 顯示原圖與旋轉圖
cv.imshow('Rotated', rotated)
cv.waitKey(0)
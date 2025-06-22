import cv2 as cv
import numpy as np
#---------------------------------------------------------------------------------
#   (0,0)
#    ●────────────→ x (橫向，向右越大)
#    │
#    │
#    ↓
#    y (縱向，向下越大)
#---------------------------------------------------------------------------------



#first one, no color, size 100x300
blank1 = np.zeros((300, 300), dtype='uint8')# blank image at new window
                                            # dtype --> data type 
                                            # uint8 meaning --> image
                                            # np.zeros((300, 300)--> grayish color only
cv.imshow('blank', blank1)
                                            
#second one, green color image, size 200x300 plus channel (RGB)
#在 OpenCV 中，顏色順序是 BGR 

blank2 = np.zeros((500, 500, 3), dtype='uint8') # np.zeros 預設值都是 [0, 0, 0] 黑色
                                                # # np.zeros(500, 500)--> grayish color only
                                                # np.zeros((500, 500, 3)--> puls 3 --> RGB color
blank2[:] = 0,255,0 

#blank2 = np.zeros 先產一張黑色圖
#blank2[100:200, 300:400] = [0,255,255] 在黑色圖上 --> 貼上特定顏色 , 指尺寸 相減[100:200, 300:400]

cv.imshow('green', blank2) #顯示整張圖
cv.waitKey(0)

#| 組合              | 顏色 |
#| \[255, 255, 255] | 白色 |
#| \[0, 0, 0]       | 黑色 |
#| \[255, 255, 0]   | 青色 |
#| \[0, 255, 255]   | 黃色 |
#| \[255, 0, 255]   | 紅色 |     
#| \[0, 255, 0]     | 綠色 |       
#| \[0, 0, 255]     | 紅色 |     





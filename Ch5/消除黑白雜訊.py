import numpy as np
import cv2

img1 = cv2.imread( "pic/sp.bmp", 0 )
img2 = cv2.medianBlur( img1, 3 )

cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Median Filtering", img2 )
cv2.waitKey( 0 )

cv2.imwrite( "output.bmp", img2 )

'''
功能:
能消除隨機出現的黑白點雜訊。
不會像均值濾波那樣模糊邊緣。
適合黑白或彩色圖片。
'''
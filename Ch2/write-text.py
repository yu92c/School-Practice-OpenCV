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
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.putText(blank, 'hello', (200,200) ,cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0), 3)

cv.imshow('text', blank)
cv.waitKey(0)
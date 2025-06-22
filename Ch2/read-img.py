# at terminal typing pwd to check location 'now'(0617).
# at termial typing cd to move location (test-env).
# display image, after run, at terminal typing python filename.py

import cv2 as cv

img = cv.imread('pic/cb.jpg')             # loading image.
cv.imshow('cb', img)                      # display image in new window ('cb' jsut title name).
cv.waitKey(0)                             # will keep showing till press esc.

# for now just using small image.
# if load large image (larger than your screen),it might go off screen.

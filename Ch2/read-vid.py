import cv2 as cv
capture = cv.VideoCapture('vid/a.mp4') #using file path
#if using webcam or camera to connect computer, at () <--integer 0 only one cam.
#multiple cam connect using 1,2,3...

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(30) & 0xff==ord('x'): #till press x on keyboard, video will stop
        break

#just run video will show on new window.
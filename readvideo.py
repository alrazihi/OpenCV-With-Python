import cv2 as cv

capture =cv.VideoCapture('videos/1.mp4')
#0 is your cam VideoCapture(0)

while True:
       isTrue, frame=capture.read()
       cv.imshow('Video', frame)

       if cv.waitKey(20) & 0xFF==ord('d'):
           #ord(d) means if d is pressed
        break
capture.release()
cv.destroyAllWindows()

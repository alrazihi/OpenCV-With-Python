import cv2 as cv


def rescaleFrame(frame,scale=0.75):
    #This works for images,videos and live videos
        width=int(frame.shape[1]*scale)
        height=int(frame.shape[0]*scale)
        dimensions =(width,height)
        return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

capture =cv.VideoCapture('videos/1.mp4')
#0 is your cam VideoCapture(0)
def changeRes(width,height):
# works only with live videos
    capture.set(3, width)
    capture.set(4, height)
while True:
       isTrue, frame=capture.read()
       videoresized = rescaleFrame(frame,scale=0.2)
       cv.imshow('Video', frame)
       cv.imshow('Video Resized', videoresized)

       if cv.waitKey(20) & 0xFF==ord('d'):
           #ord(d) means if d is pressed
        break
capture.release()
cv.destroyAllWindows()

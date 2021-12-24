import cv2 as cv
import numpy as np

img =cv.imread('photos/1.png')
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)
#blank[:]=0,255,0
blank[200:300,300:400]=0,255,0
cv.imshow('Green', blank)
cv.rectangle(blank, (0,0), (250,500), (0,255.0),thickness=cv.FILLED)
#thickness=cv.filled fil the screen
cv.imshow('Rec', blank)

circle=cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,250))
cv.imshow("Circle", circle)
line=cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255),thickness=3)
cv.imshow("line", line)

text=cv.putText(blank, "Alrazihi", (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255),2)

cv.imshow("Text", text)
cv.waitKey(0)
import cv2
import numpy as np

cap = cv2.VideoCapture('/home/samia/Documents/OpenCV/ComputerVision-OpenCv-/VideoCapture/sam.mp4')

#check if camera opened successfully

if(cap.isOpened()==False):
    print("Error opening video file")

#read until video is completed

while(cap.isOpened()):
    #capture frame by frame
    ret,frame=cap.read()
    if ret == True:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

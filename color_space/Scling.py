import cv2
import numpy as np

file_name ="/home/samia/Documents/OpenCV/color_space/c.jpeg"
try:
    img = cv2.imread(file_name)
    (height,width)=img.shape[:2]

    res = cv2.resize(img,(int(width/2),int(height/2)),interpolation=cv2.INTER_CUBIC)
    (rows,cols)=img.shape[:2]

    M=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
    res=cv2.wrapAffine(img,M,(cols,rows))

    cv2.imwrite('result.jpg',res)
    cv2.imshow('input',img)
    cv2.waitKey(0)
    cv2.imshow('output',res)
    cv2waitKey(0)

except IOError:
    print('Error while reading files !!!')

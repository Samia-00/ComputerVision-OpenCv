import cv2
import numpy as np
file_name ="/home/samia/Documents/OpenCV/color_space/c.jpeg"
try:
    img = cv2.imread(file_name)
    edges=cv2.Canny(img,100,200)

    cv2.imwrite('res.jpg',edges)
    cv2.imshow('output',edges)
    cv2.waitKey(0)
except IOError:
    print('Error while reading!!!!!!!!')

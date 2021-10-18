import cv2
import numpy as np

image = cv2.imread('/home/samia/Documents/OpenCV/color_space/c.jpeg')
'''
cv2.imshow('Original Image',image)
cv2.waitKey(0)
'''
Gaussian =cv2.GaussianBlur(image,(7,7),0)
cv2.imshow('Gaussian Blurring',Gaussian)
cv2.waitKey(0)


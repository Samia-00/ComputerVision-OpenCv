import cv2
import numpy as np

image = cv2.imread('/home/samia/Documents/OpenCV/color_space/c.jpeg')

median =cv2.medianBlur(image,5)
cv2.imshow('Median Blurring',median)
cv2.waitKey(0)

import cv2
import numpy as np

image = cv2.imread('/home/samia/Documents/OpenCV/color_space/c.jpeg')

bilateral =cv2.bilateralFilter(image,9,75,75)
cv2.imshow('bilateral Blurring',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

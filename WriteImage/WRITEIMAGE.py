import cv2
import argparse
import numpy as np
image = cv2.imread("image.jepg")

#(h,w)=image.shape

#print("Height = {} , width = {}".format(h,w))


window_name = 'image'

cv2.imshow(window_name,image)








cv2.waitKey(0)
cv2.destroyAllWindows()

imr=cv2.resize(image,(80,80))


filename="test.jepg"
cv2.imwrite(filename,imr)

import cv2
image = cv2.imread("/home/samia/Documents/OpenCV/WriteImage/image.jpeg")
window_name = 'image'
(h,w)=image.shape[:2]
print("Height = {} , width = {}".format(h,w))

#cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()

imr=cv2.resize(image,(80,80))
filename="test.jpg"
cv2.imwrite(filename,imr)

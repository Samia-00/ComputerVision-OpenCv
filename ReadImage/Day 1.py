import cv2
#image = cv2.imread('/home/samia/Documents/OpenCV/image.jpg')
image = cv2.imread('image.jpeg')
window_name ="Display Image"
cv2.imshow(window_name,image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
image = cv2.imread('image.jpeg')
window_name ="Display Image"

img=cv2.imread("image.jpeg",cv2.IMREAD_COLOR)
cv2.imshow(window_name,img)

cv2.waitKey(0)
cv2.destroyAllWindows()

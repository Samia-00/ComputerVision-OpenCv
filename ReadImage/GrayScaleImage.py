import cv2
image = cv2.imread('image.jpeg')
window_name ="Display Image"
image=cv2.imread("image.jpeg",cv2.IMREAD_GRAYSCALE)

cv2.imshow(window_name,image)

cv2.waitKey(0)
cv2.destroyAllWindows()

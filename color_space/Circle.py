import cv2

path = "/home/samia/Documents/OpenCV/color_space/w.jpeg"

image = cv2.imread(path)
window_name = "Image"

center_coordinates=(300,150)
radius =100
color =(255,255,0)
thickness=10
image=cv2.circle(image,center_coordinates,radius,color,thickness)
cv2.imshow(window_name,image)
cv2.waitKey(0)

cv2.destroyAllWindows()

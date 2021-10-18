import cv2

path = "/home/samia/Documents/OpenCV/color_space/w.jpeg"

image=cv2.imread(path)
window_name ='Image'

start_point =(100,100)

end_point=(200,250)
color =(255,0,0)
thickness =10
image = cv2.rectangle(image,start_point,end_point,color,thickness)
cv2.imshow(window_name,image)

cv2.waitKey(0)

cv2.destroyAllWindows()

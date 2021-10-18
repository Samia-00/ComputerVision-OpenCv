import cv2
path="/home/samia/Documents/OpenCV/color_space/image.jpeg"
image=cv2.imread(path)
window_name='image'

start_point =(100,250)

end_point=(50,20)

color=(0,255,0)
thickness =9
image = cv2.line(image,start_point,end_point,color,thickness)
cv2.imshow(window_name,image)

cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2

path="/home/samia/Documents/OpenCV/color_space/w.jpeg"

image= cv2.imread(path)

window_name ='Image'
font = cv2.FONT_HERSHEY_SIMPLEX

ORG = (250,250)

fontScale = 1
color = (255,0,0)

thickness=10

image = cv2.putText(image,'PYTHON OPEN-CV',ORG,font,fontScale,color,thickness)

cv2.imshow(window_name,image)

cv2.waitKey(0)

cv2.destroyAllWindows()

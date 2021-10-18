import cv2
path="/home/samia/Documents/OpenCV/color_space/c.jpeg"

image=cv2.imread(path)
window_name ='Image'
'''
image=cv2.copyMakeBorder(image,5,10,5,10,cv2.BORDER_CONSTANT,None)
cv2.imshow(window_name,image)
cv2.waitKey(0)
'''
image=cv2.copyMakeBorder(image,100,100,50,50,cv2.BORDER_REFLECT)
cv2.imshow(window_name,image)
cv2.waitKey(0)

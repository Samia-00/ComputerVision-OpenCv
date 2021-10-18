import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade= cv2.CascadeClassifier('/home/samia/Documents/OpenCV/ComputerVision-OpenCv-/VideoCapture/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/samia/Documents/OpenCV/ComputerVision-OpenCv-/VideoCapture/data/haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('/home/samia/Documents/OpenCV/ComputerVision-OpenCv-/VideoCapture/data/haarcascades/haarcascade_smile.xml')

def adjusted_detect_face(img):
    face_img=img.copy()
    face_rect = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in face_rect:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
    return face_img


def detect_eyes(img):
    eye_img=img.copy()
    eye_rect=eye_cascade.detectMultiScale(eye_img,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in eye_rect:
        cv2.rectangle(eye_img,(x,y),(x+w,y+h),(255,255,255),10)
    return eye_img

img1=cv2.imread('/home/samia/Documents/OpenCV/ComputerVision-OpenCv-/VideoCapture/girl.jpg')
    
img_copy1=img1.copy()
img_copy2=img1.copy()
img_copy3 =img1.copy()

face =adjusted_detect_face(img1)
plt.imshow(face)

window_name='face'
cv2.imwrite('face.jpg',face)
cv2.imshow(window_name,face)

eyes = detect_eyes(img_copy2)
plt.imshow(eyes)
window_name1='eyes.jpg'
cv2.imwrite('eyes.jpg',eyes)
cv2.imshow(window_name1,eyes)

eyes_face = adjusted_detect_face(img_copy3)
eyes_face = detect_eyes(eyes_face)
plt.imshow(eyes_face)
window_name2='face+eyes.jpg'

cv2.imwrite('face+eyes.jpg',eyes_face)
cv2.imshow(window_name2,eyes_face)

cv2.waitKey(0)
cv2.destroyAllWindows()













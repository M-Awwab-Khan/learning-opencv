import cv2
import numpy as np

img = cv2.imread('resources/lena.png')
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7, 7), 0)
imgCanny = cv2.Canny(img, 150, 150)
imgDialation = cv2.dilate(img,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blurred Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.waitKey(0)
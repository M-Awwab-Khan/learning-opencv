import cv2

img = cv2.imread('resources/lena.png')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7, 7), 0)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blurred Image",imgBlur)
cv2.waitKey(0)
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

# width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

# Calculate the width and height based on the bounding box of pts1
width = int(max(pts1[1][0] - pts1[0][0], pts1[3][0] - pts1[2][0]))
height = int(max(pts1[2][1] - pts1[0][1], pts1[3][1] - pts1[1][1]))
print(width, height)

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
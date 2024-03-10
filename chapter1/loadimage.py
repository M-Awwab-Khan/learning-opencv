import cv2
print("package imported")

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)
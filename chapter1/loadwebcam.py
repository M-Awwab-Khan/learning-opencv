import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth) #width
cap.set(4, frameHeight) #height
cap.set(10, 150) #brightness

while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
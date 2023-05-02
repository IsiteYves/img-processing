import cv2

# Load the image
img = cv2.imread('lena.jpg')

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect the face in the image
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

# Crop the face and display it
for (x, y, w, h) in faces:
    cropped = img[y:y+h, x:x+w]
    cv2.imshow('Cropped Face', cropped)
    cv2.waitKey(0)

cv2.destroyAllWindows()

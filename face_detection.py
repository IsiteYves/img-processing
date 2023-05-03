import cv2

# Load the image
img = cv2.imread('em1.png')

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect the face in the image
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

# Save each cropped face with a different name
counter = 1
for (x, y, w, h) in faces:
    cropped = img[y:y+h, x:x+w]
    cv2.imshow('Cropped Face', cropped)
    cv2.imwrite("cropped_face_{}.jpg".format(counter), cropped)
    counter += 1
    cv2.waitKey(0)

cv2.destroyAllWindows()

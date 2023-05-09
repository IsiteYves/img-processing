import cv2

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a VideoCapture object for the default camera (index 0)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Read frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Convert the frame to grayscale for faster face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Apply funny effects to each detected face
        for (x, y, w, h) in faces:
            # Draw a green rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Make the eyes look bigger by scaling them up
            eyes = frame[y:y+h, x:x+w]
            eyes = cv2.resize(eyes, None, fx=1.5, fy=1.5,
                              interpolation=cv2.INTER_LINEAR)
            frame[y:y+h, x:x+w] = eyes

            # Add a funny hat to the head
            hat = cv2.imread('funny_hat.png', cv2.IMREAD_UNCHANGED)
            hat_resized = cv2.resize(hat, (w, h))
            hat_alpha = hat_resized[:, :, 3] / 255.0
            hat_bgr = hat_resized[:, :, 0:3]
            hat_overlay = hat_alpha[..., np.newaxis] * hat_bgr
            hat_overlay = hat_overlay.astype(np.uint8)
            frame[y:y+h, x:x +
                  w] = cv2.addWeighted(frame[y:y+h, x:x+w], 1.0, hat_overlay, 0.8, 0)

        # Display the frame
        cv2.imshow('Funny Face', frame)

        # Wait for key press and exit if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

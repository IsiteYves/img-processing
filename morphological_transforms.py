import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Resize the frame
    resized = cv2.resize(frame, (800, 650))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    # Define a structuring element (in this case a rectangular kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Apply the erosion transformation
    erosion = cv2.erode(gray, kernel, iterations=1)

    # Apply the dilation transformation
    dilation = cv2.dilate(gray, kernel, iterations=1)

    # Display the original and transformed images side by side
    combined = cv2.hconcat(
        [resized, cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)])
    cv2.imshow('Live Video', combined)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

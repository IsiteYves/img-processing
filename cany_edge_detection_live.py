import cv2

# Initialize video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Detect edges using Canny edge detection
    edges = cv2.Canny(frame, 100, 200)

    # Resize the image to (800, 650)
    resized = cv2.resize(edges, (800, 650))

    # Resize the frame to (800, 650)
    frame_resized = cv2.resize(frame, (800, 650))

    # Combine the resized frame and the resized edge detection image horizontally
    combined = cv2.hconcat(
        [frame_resized, cv2.cvtColor(resized, cv2.COLOR_GRAY2BGR)])

    # Display the combined image
    cv2.imshow('Edges and Webcam Feed', combined)

    # Check if 'q' key is pressed to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

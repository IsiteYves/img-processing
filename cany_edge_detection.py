import cv2

# Load the image
img = cv2.imread('lena.jpg')

# Detect edges using Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Resize the image to (800, 650)
resized = cv2.resize(edges, (800, 650))

# Display the resized image
cv2.imshow('Resized Edges', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

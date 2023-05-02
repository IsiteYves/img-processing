import cv2
img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ', img.shape)
scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

edges = cv2.Canny(resized, 100, 200)

# Save resized image
cv2.imwrite("lena_resized.jpg", edges)

# print('Resized Dimensions : ', resized.shape)
cv2.imshow("Resized image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

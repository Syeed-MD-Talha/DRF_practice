import cv2

# Read the image with flag for color image
img = cv2.imread('spiderman.jpg', flags=0)

cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('graySpiderman.png',img)
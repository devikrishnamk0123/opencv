import cv2
import numpy as np
# eroding means eroding away the boundaries of a foreground object in white color
# using a kernel. A pixel in the original image is considered 1 if all pixels coming under the kernel is 1.
# else, the pixel value is made to 0 or eroded.
# all pixels near the boundary will get eroded depending on the boundary size.
# to perform erosion, input image must be in GRAY_SCALE mode.

image1 = cv2.imread("apple_icon.jpeg", 0)  # reads image in gray scale mode.
cv2.imshow("Original Image", image1)
cv2.waitKey(0)
kernel1 = np.ones((5, 5), np.uint8)
erosion = cv2.erode(image1, kernel1, iterations=1)
cv2.imshow("Eroded Image", erosion)
cv2.waitKey(0)

cv2.destroyAllWindows()

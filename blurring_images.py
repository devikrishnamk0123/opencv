# different blurring methods:
# Homogeneous filter : each output pixel is the mean of its kernel neighbours
# Gaussiean filter : using different weighted kernel in both x and y direction.
# Median Filter : replaces each pixel value with the median of its neighbouring pixels. used when salt and pepper noise is present.
# Bilateral filter

import cv2
import numpy as np
image1 = cv2.imread("/Users/devikrishnamk/Desktop/microsoft.png", 1)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)  # numpy needs rgb format.
kernel1 = np.ones((5, 5), np.float32)/25

convoluted_2d_image = cv2.filter2D(image1, -1, kernel1)  # 2d convolution
gaussian_blurred_image = cv2.GaussianBlur(image1, (5, 5), 0)
median_blurred_image = cv2.medianBlur(image1, 5)
bilateral_filtered_image = cv2.bilateralFilter(image1, 9, 75, 75)
cv2.imshow("Original image", image1)
cv2.waitKey(0)
cv2.imshow("2 D convoluted image", convoluted_2d_image)
cv2.waitKey(0)
cv2.imshow("Gaussian blurred image", gaussian_blurred_image)
cv2.waitKey(0)
cv2.imshow("Median blurred image", median_blurred_image)
cv2.waitKey(0)
cv2.imshow("Bilateral filtered image", bilateral_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

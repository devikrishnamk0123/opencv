# open cv reads images specified as read in COLOR format in bgr format.
import cv2

import numpy as np
# 1 indicates read in COLOR format
original_image = cv2.imread("/Users/devikrishnamk/Desktop/microsoft.png", 1)
# 0 indicates read in GRAY_SCALE format
# -1 indcates read through alpha channel
original_to_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
original_to_hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
original_to_brightlab = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)

cv2.imshow("Original image", original_image)
cv2.waitKey(0)
cv2.imshow("Gray image", original_to_gray)
cv2.waitKey(0)
cv2.imshow("Hsv image", original_to_hsv)
cv2.waitKey(0)
# words written inside double quotes is to display the title of the image window
cv2.imshow("Lab image", original_to_brightlab)

# time in milliseconds for which the window is displayed. if 0 is given, the window is active until any key is pressed.
cv2.waitKey(0)
cv2.destroyAllWindows()

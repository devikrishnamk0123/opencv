import cv2
# to apply bitwise operations, images should be of same size.
# AND : is true when both pixel values are greater than 0.
# OR : is true when either of the pixel values are greater than 0.
# XOR : is true when either one of the pixel value is greater than 0 and not both.
# NOT : is true when the pixel value is 0. False when pixel value is > 0.

image1 = cv2.imread("apple_icon.jpeg", cv2.IMREAD_COLOR)
image2 = cv2.imread("/Users/devikrishnamk/Desktop/microsoft.png", 1)
image1 = cv2.resize(image1, (225, 225))

bitwise_and_image = cv2.bitwise_and(image1, image2)
cv2.imshow("AND", bitwise_and_image)
cv2.waitKey(0)

bitwise_or_image = cv2.bitwise_or(image1, image2)
cv2.imshow("OR", bitwise_or_image)
cv2.waitKey(0)

bitwise_xor_image = cv2.bitwise_xor(image1, image2)
cv2.imshow("XOR", bitwise_xor_image)

not_image1 = cv2.bitwise_not(image1)
cv2.imshow("NOT", not_image1)
cv2.waitKey(0)

not_image2 = cv2.bitwise_not(image2)
cv2.imshow("NOT image 2", not_image2)
cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2
image = cv2.imread("apple_icon.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("Icon",image)
key = cv2.waitKey(0)
cv2.destroyAllWindows()


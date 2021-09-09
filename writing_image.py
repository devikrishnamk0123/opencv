import cv2
image = cv2.imread("/Users/devikrishnamk/Desktop/microsoft.png",1)
cv2.imwrite("microsoft.jpg",image) # writes the image from desktop to the current working directory
cv2.imshow("Microsoft Icon",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
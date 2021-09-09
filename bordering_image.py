# border types are:
# BORDER_CONSTANT : adds a constant colored border. value of color should be specified
# BORDER_REFLECT : adds mirrored reflections of the border elements in the respective sides.
# BORDER_REPLICATE : replicates the last element.
import cv2
image1 = cv2.imread("/Users/devikrishnamk/Desktop/microsoft.png", 1)
colored_border = cv2.copyMakeBorder(image1, 5, 5, 4, 4, cv2.BORDER_CONSTANT, 1)
reflected_border = cv2.copyMakeBorder(image1, 5, 5, 4, 4, cv2.BORDER_REFLECT)
replicated_border = cv2.copyMakeBorder(
    image1, 5, 5, 4, 4, cv2.BORDER_REPLICATE)

cv2.imshow("Colored border", colored_border)
cv2.waitKey(0)
cv2.imshow("reflected border", reflected_border)
cv2.waitKey(0)
cv2.imshow("replicated border", replicated_border)
cv2.waitKey(0)
cv2.destroyAllWindows()

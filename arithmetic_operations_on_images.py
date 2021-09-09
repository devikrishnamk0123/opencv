import cv2
# channel in image is the grayscale image of the original image made of one of the primary colors.
# colored_images are 3 channeled. i.e each pixel consists of 3 values.representing the primary colors.
# but gray scaled image has each pixel with a single value which is the amount of intensity of light.
# black and white images have pixel values as 0 or 1. also called binary images.
image1 = cv2.imread("apple_icon.jpeg", cv2.IMREAD_COLOR)
image2 = cv2.imread("/Users/devikrishnamk/Desktop/microsoft.png", 1)
dimensions_of_image1 = image1.shape
print(dimensions_of_image1[0],
      dimensions_of_image1[1], dimensions_of_image1[2])

# to get the dimensions of the image. Height is at index 0. Width is at index 1. Number of channels at index 3.
dimensions_of_image2 = image2.shape
print(dimensions_of_image2[0],
      dimensions_of_image2[1], dimensions_of_image2[2])

# to add 2 images, their dimensions must be same.
image1 = cv2.resize(image1, (225, 225))
added_image = image1 + image2

# adding weights to images. as weight increases, that image becomes more prominent.total weight of both images = 1 always. Gamma value = 0.
added_image_using_weight = cv2.addWeighted(image1, 0.1, image2, 0.9, 0)
cv2.imshow("Added image", added_image)
cv2.waitKey(0)
cv2.imshow("Weighted added image", added_image_using_weight)
cv2.waitKey(0)
cv2.destroyAllWindows()

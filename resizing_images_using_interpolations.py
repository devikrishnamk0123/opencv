import cv2
# to zoom in : use cv2.INTER_LINEA"apple_icon.jpeg", cv2.IMREAD_COLOR interpolation method.
# to shrink or enlarge : use cv2.INTER_AREA and specify the required dimensions in the resize method.
# cv2.INTER_CUBIC is slow but more efficient

image1 = cv2.imread("apple_icon.jpeg", cv2.IMREAD_COLOR)
image1_dimensions = image1.shape
height_of_image1 = image1_dimensions[0]
width_of_image1 = image1_dimensions[1]
print("Original height: ", height_of_image1)
print("Original width", width_of_image1)
cv2.imshow("original image", image1)
cv2.waitKey(0)

area_interpolated = cv2.resize(
    image1, (225, height_of_image1), interpolation=cv2.INTER_AREA)
cv2.imshow("area interpolated", area_interpolated)
cv2.waitKey(0)
area_interpolated_dimensions = area_interpolated.shape
height_of_area_interpolated = area_interpolated_dimensions[0]
width_of_area_interpolated = area_interpolated_dimensions[1]
print("Area interpolated height: ", height_of_area_interpolated)
print("Area interpolated width: ", width_of_area_interpolated)

linear_interpolated = cv2.resize(
    image1, (width_of_image1, height_of_image1), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linear interpolated", linear_interpolated)
cv2.waitKey(0)
linear_interpolated_dimensions = linear_interpolated.shape
height_of_linear_interpolated = linear_interpolated_dimensions[0]
width_of_linear_interpolated = linear_interpolated_dimensions[1]
print("Linear interpolated height: ", height_of_linear_interpolated)
print("Linear interpolated width: ", width_of_linear_interpolated)

cv2.destroyAllWindows()

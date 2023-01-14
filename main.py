import cv2 
from helper_functions import encode, decode_image

img = cv2.imread("dollar_img.tif", 0)

hidden_message = "this bank is going to be robbed"

encoded_image = encode(img, hidden_message)

cv2.imwrite("coded_image.png", encoded_image)

image_encoded = cv2.imread("coded_image.png")
decoded_message = decode_image(image_encoded)

print("Decoded message - ", decoded_message)
cv2.imshow("Original Image", img)
cv2.imshow("Encoded image", encoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
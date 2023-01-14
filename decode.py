import cv2 
from helper_functions import decode_image
import argparse
import math

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('image',
                    help='path of image')
parser.add_argument('-s', '--show', action='store_true', 
                    help = "show hidden text on image")
args = parser.parse_args()

img = cv2.imread(args.image)
decoded_message = decode_image(img)
height, width = img.shape[:2]




print("Decoded Message - ")
print(decoded_message)

if args.show:
    FONT_SCALE = 2  # Adjust for larger font size in all images
    THICKNESS_SCALE = 1e-2  # Adjust for larger thickness in all images

    font_scale = min(width, height) * FONT_SCALE
    thickness = math.ceil(min(width, height) * THICKNESS_SCALE)
    cv2.putText(img, decoded_message, (width//5, 5*height//6), cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, (0, 0, 255), thickness, cv2.LINE_AA)
    cv2.imshow("Decoded image", img)
    cv2.waitKey(0)
    im_save = args.image[:-4]
    im_save = im_save + "_decoded.png"
    cv2.imwrite(im_save, img)

cv2.destroyAllWindows()

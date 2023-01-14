# Script to run encode from comman line 
import cv2 
from helper_functions import encode, decode_image
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--image',
                    help='path of image')
parser.add_argument('-m', '--message',
                    help='path of image')
parser.add_argument('-s', '--save_location', default="encoded_image.png",
                    help='saved_location of the image')

args = parser.parse_args()

img = cv2.imread(args.image)

hidden_message = args.message

encoded_image = encode(img, hidden_message)
# cv2.imshow("coded image", encoded_image)
# cv2.waitKey(0)
if cv2.imwrite("images/" + args.save_location, encoded_image):
    print("Message coded, and saved in ","images/" + args.save_location)
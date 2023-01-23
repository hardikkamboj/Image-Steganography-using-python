# Image-Steganography-using-python-hiding-data-in-image-
An End-to-End program written in python which allows us to hide data in images

![image](https://miro.medium.com/max/1400/1*dQyfOpFWmSxrmdOcQgW6OQ.jpeg)

## The Approach
An image is made up of pixels, and these pixels are stored as an 8-bit integer. We can further split individual pixels into their bit planes, starting from MSB (most significant bit) to LSB (least significant bit). 

Most of the information is stored in the MSB, so, any change made in MSB will result in a huge change in the pixel value. But, we can change the LSB, and still, the overall pixel value won't change much.

Using this information, we can embed any hidden message in the LSB of the pixels, and the overall image will look the same. 

In this program, we first see how we can approach this problem, step by step method is mentioned in the [jupyter notebook](Image__Steganography.ipynb) , then once the aprroach is final, we will make it into a script through which we can run it from terminal without the need of going into the code. 

Video - [Code walkthrough](https://youtu.be/5M3kjYLShlk)
## Terminal run

To Encode message in Image - 
```
python encode.py -i image_path -m "message to be encoded" -s save_location
```

To decode the hidden image - 
```
python decode.py image_path 
```
To show output on image 
```
python decode.py image_path --show
```

To know the approach used, go through the notebook [Image__Steganography.ipynb](Image__Steganography.ipynb). 

## Example

Given the following image, 

![](bharat_mata.png)

we want to decode the message saying "Vanday Matram", 

`python encode.py -i bharat_mata.png -m "Vanday Matram" -s image_encoded.png`

which can later be decoded by the command -

`python decode.py images/image_encoded.png`

To visualize the hidden message on the image, use - 
`python decode.py images/image_encoded.png --show`

The final image will contain the hidden message 

![](images/image_encoded_decoded.png)

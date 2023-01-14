# Image-Steganography-using-python-hiding-data-in-image-
An End-to-End program written in python which allows us to hide data in images

![image](https://miro.medium.com/max/1400/1*dQyfOpFWmSxrmdOcQgW6OQ.jpeg)

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


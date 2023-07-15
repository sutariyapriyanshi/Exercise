# Python program to find the size(Resolution) of the image

import PIL
from PIL import Image

img=PIL.Image.open("C:/Users/Priyanshi Sutariya/Desktop/selfie.png")

width,height=img.size

print(width,"X",height)

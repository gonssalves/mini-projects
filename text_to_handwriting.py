import pywhatkit as kit
from PIL import Image

hand_written = input('Enter your text to convert in Handwriting: ')

#converting handwritten and saving
kit.text_to_handwriting(hand_written, save_to='handwriting.png')

#to open the image
Image.open('clcoding.png')
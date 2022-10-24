import os
import pytesseract
from PIL import Image

image_path = 'data/test.jpg'

def extractTextFromImage(image_path):
    if image_path == None:
        raise ValueError("path is none")
    image = Image.open(image_path)
    txt = pytesseract.image_to_string(image, lang='deu')        
    return txt
    
if __name__ == '__main__':
    txt = extractTextFromImage(image_path)
    print(txt)
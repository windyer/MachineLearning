#coding:utf-8
#Test one page
import pytesseract
from PIL import Image

def processImage():
    image = Image.open('11.png')

    #背景色处理，可有可无
    image = image.point(lambda x: 0 if x < 143 else 255)
    newFilePath = '22.png'
    image.save(newFilePath)

    content = pytesseract.image_to_string(Image.open(newFilePath), lang='chi_sim')
    #中文图片的话，是lang='chi_sim'
    print(content)

processImage()
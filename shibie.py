# coding:utf-8
# Test one page
import pytesseract
from PIL import Image
import time


def processImage(img_name):
    print time.time()
    img = Image.open(img_name)
    id_1 = (305, 235, 430, 265)
    id_2 = (645,235,770,265)
    id_3 = (990, 235, 1110, 265)
    score_1 =(305,570,430,600)
    score_2 =(645,570,770,600)
    score_3 =(990,570,1110,600)

    id_img_1 = img.crop(id_1)
    id_img_2 = img.crop(id_2)
    id_img_2.save("id2.jpg")
    id_img_3 = img.crop(id_3)
    score_img_1 = img.crop(score_1)
    score_img_2 = img.crop(score_2)

    score_img_3 = img.crop(score_3)
    score_img_3.save("score3.jpg")
    image = score_img_3.point(lambda x: 0 if x < 180 else 255)
    image.save("score333.jpg")
    content = pytesseract.image_to_string(image, lang='chi_sim')
    print content
    #img_list=[id_img_1,id_img_2,id_img_3,score_img_1,score_img_2,score_img_3]
    # 背景色处理，可有可无
    #for i in img_list:
    #    image = img.point(lambda x: 0 if x < 143 else 255)
    #    content = pytesseract.image_to_string(image, lang='eng',config="0123456789")
    # 中文图片的话，是lang='chi_sim'
    #    print time.time()
    #    print(content)


processImage('1.jpg')
#coding=utf8
# 引入文字识别OCR SDK
from aip import AipOcr
import time
from PIL import Image
import re
mode = re.compile(r'\d+')
# 定义常量
APP_ID = '9779475'
API_KEY = '90piMi0OrGZfGj1HKE89edmy'
SECRET_KEY = 'rhPankPPI9CaGgjPFLWRtE6pH8uKLVLn'
# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 读取图片
def get_file_content(filePath):
    #sImg = Image.open(filePath)
    #w, h = sImg.size
    #print w, h
    #dImg = sImg.resize((int(w /1.5), int(h /1.5)), Image.ANTIALIAS)  # 设置压缩尺寸和选项，注意尺寸要用括号
    #dImg.save("score222.jpg")  # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
    with open(filePath, 'rb') as fp:
        return fp.read()
def baidu_aip(filePath):
    # 定义参数变量
    options = {
      'detect_direction': 'true',
      'language_type': 'CHN_ENG',
    }

    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    s= result['words_result']

    for i in s:
        print i['words']
    return s
print time.time()
result=baidu_aip("1.jpg")
re_d = re.compile(r'\d+')
#re_d.findall(str1)
res_dic={}
di_1=result[5]['words']
di_2=result[6]['words']
di_3=result[7]['words']
sor_1=result[-3]['words']
sor_2=result[-2]['words']
sor_3=result[-1]['words']
print di_1,di_2,di_3,sor_1,sor_2,sor_3
print time.time()
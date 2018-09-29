# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

# 从网站爬取验证码，然后转换为JPG格式保存

from urllib import request
from PIL import Image
import os

path_save = "../data/images/for_test/"

url_vericode = "https://portal1.ecnu.edu.cn/cas/code"

for i in range(20):
    # 请求响应获取图片
    request.urlretrieve(url_vericode, path_save + "test.jpg")

    # 存储为 jpg
    img_get = Image.open(path_save + "test.jpg")

    img_test = Image.new("RGB", img_get.size, (255, 255, 255))
    img_test.paste(img_get)
    print(path_save + "vericode_" + str(i+1) + ".jpg")
    img_test.save(path_save + "vericode_" + str(i+1) + ".jpg")

    # delete the saved images
    os.remove(path_save + "test.jpg")

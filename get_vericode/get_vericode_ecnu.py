# 从网站爬取验证码，然后转换为JPG格式保存

from urllib import request
import cv2
from PIL import Image

path_save = "F:/code/python/P_web_spider/data/pics/ecnu_vericodes/"

url_ecnu_vericode = "https://portal1.ecnu.edu.cn/cas/code"

# 请求响应获取图片
request.urlretrieve(url_ecnu_vericode, path_save+"test.jpg")

# 存储为jpg
img_veri = Image.open(path_save+"test.jpg")

# background = Image.new("RGB", img_veri.size, (255, 255, 255))
# background.paste(img_veri)
# background.save(path_save+"code_"+str(cnt)+".jpg")
# print("code_"+str(cnt)+".jpg")
# print(background.format)
#

#im_cv2 = cv2.imread(path_save+"code_1.jpg")
#print(im_cv2.shape)
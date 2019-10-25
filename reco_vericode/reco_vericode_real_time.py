# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

# 从网站爬取验证码

import cv2
import numpy as np

from urllib import request
from PIL import Image
from reco_vericode import tools

########## web spider to get vericode ########

path_save = "../data/images/for_test/"

# url_vericode = "https://portal1.ecnu.edu.cn/cas/code"
url_vericode = "http://lxs.ecnu.edu.cn/EN/book.php?act=chkcode"

# 请求响应获取图片
request.urlretrieve(url_vericode, path_save + "test.jpg")

# 存储为 jpg
img_get = Image.open(path_save + "test.jpg")
print(img_get.size)
img_PIL = Image.new("RGB", img_get.size, (255, 255, 255))
img_PIL.paste(img_get)

# convert PIL to OpenCv
img_PIL = img_PIL.convert('RGB')
img_cv2 = np.array(img_PIL)
img_cv2 = img_cv2[:, :, ::-1].copy()

############# decode vericode  #############
decoded_num = tools.decode_vericode(img_cv2)

# print(img_cv2.shape)
cv2.putText(img_cv2, str(decoded_num), (20, 52), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow("img_show", img_cv2)
cv2.namedWindow("img_show")
cv2.waitKey(0)
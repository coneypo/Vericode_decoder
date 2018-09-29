# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

import cv2

from reco_vericode import tools

img_test = cv2.imread("../data/images/for_test/vericode_1.jpg")

tools.decode_vericode(img_test)

# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

import os
import cv2
from reco_vericode import tools


vericode_to_decode_list = os.listdir("../data/images/for_test/")
vericode_to_decode_list.sort()

for vericode_to_decode in vericode_to_decode_list:
    img_test = cv2.imread("../data/images/for_test/"+vericode_to_decode)

    print(vericode_to_decode)
    tools.decode_vericode(img_test)
    print('\n')
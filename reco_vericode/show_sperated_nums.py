# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

# show bounding rectangles of image

import cv2
import numpy as np

path_test_image = "../data/images/for_test/vericode_2.jpg"


def show_bounding_rect(path_image):

    img = cv2.imread(path_image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # 返回三个值，图像，轮廓，轮廓的层析结构
    image, contours, hierarchy = cv2.findContours(img_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Nums of contours:", len(contours), "\n")
    contours_list = []

    # ii = 0,1,2,3
    for ii in range(len(contours)):
        contours_list.append(contours[3 - ii])

    # 外矩阵
    # cv2.boundingRect 计算轮廓的垂直边界最小矩形
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours_list[i])
        print("Number:", i+1)
        print("Position:(", x, ",", y, ')\t', "(", x + w, ",", y + h, ")")
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        print('\n')
    print('\n')

    cv2.imshow("img", img)
    cv2.waitKey(0)


show_bounding_rect(path_test_image)
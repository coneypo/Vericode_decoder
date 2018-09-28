

import os
import cv2
import numpy as np

from PIL import Image
from sklearn.externals import joblib


# ml model的位置
path_models = "F:/code/python/P_web_spider/ML_handwritten_nums/ml_models/"

# 提取单张图像的特征
def get_features_single(img):
    # 转为灰度
    img = img.convert('1')

    # 提取特征
    # 30*30的图像
    pixel_cnt_list = []

    height, width = 30, 30
    # 统计30行每行的黑点数
    for y in range(height):
        pixel_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:  # 黑点
                pixel_cnt_x += 1
        pixel_cnt_list.append(pixel_cnt_x)
    # 统计30列每列的黑点数
    for x in range(width):
        pixel_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:  # 黑点
                pixel_cnt_y += 1
        pixel_cnt_list.append(pixel_cnt_y)
    return pixel_cnt_list

# 输入路径，返回
def get_num(path_test):

    # 图像分割
    img_rd = cv2.imread(path_test)
    # 二值化
    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)
    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
    # 返回三个值，图像，轮廓，轮廓的层析结构
    image, contours, hierarchy = cv2.findContours(img_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_4 = []
    contours_4.append(contours[3])
    contours_4.append(contours[2])
    contours_4.append(contours[1])
    contours_4.append(contours[0])

    path_save = "F:/code/python/P_web_spider/data/pics/single_pic_4_parts/"

    LR = joblib.load(path_models + "model_LR_1.m")

    # 外界矩阵
    # cv2.boundingRect 计算轮廓的垂直边界最小矩形

    tmp_num = ""  # 存储解析出来的数字

    for i1 in range(4):
        x, y, w, h = cv2.boundingRect(contours_4[i1])
       # print("pos:", x, ",", y, '\t', x + w, ",", y + h)
        img_rd = cv2.rectangle(img_rd, (x, y), (x + w, y + h), (0, 255, 0), 1)

        height = h
        width = w

        img_blank = np.zeros((30, 30, 3), np.uint8)

        # 生成一张新的空白背景的图像
        for ii1 in range(0, 30):
            for jj1 in range(0, 30):
                # img_rd [height高度][width宽度]
                img_blank[ii1][jj1] = (255, 255, 255)

        # 写入分割下来的数据
        for ii2 in range(0, height + 5):
            for jj2 in range(0, width + 5):
                # img_rd [height高度][width宽度]
                img_blank[ii2 + 5][jj2 + 5] = img_rd[y + ii2][x + jj2]

        # 获取分割图像的特征
        path_single_num = path_save + "img_nums_" + str(i1 + 1) + ".png"
    #    cv2.imwrite(path_single_num, img_blank)

       # print(path_single_num)
    #    tmp_pic = Image.open(path_single_num)
        tmp_pic = Image.fromarray(img_blank)

        # 获取特征，调用模型计算
        features_single = get_features_single(tmp_pic)
        predict_LR = LR.predict([features_single])
        tmp_num = tmp_num+(str(predict_LR[0]))

    print(int(tmp_num))
    return int(tmp_num)

# 测试图片的位置
path_test = "F:/code/python/P_web_spider/data/pics/ecnu_vericodes/"

get_num(path_test+"code_26.jpg")

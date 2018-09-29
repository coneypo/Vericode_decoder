# 提取单张图像的特征
def get_features_single(img):
    # 转为灰度
    img = img.convert('1')

    # 提取特征
    # 30*30 的图像
    pixel_cnt_list = []

    height, width = 30, 30

    # 统计 30 行每行的黑点数
    for y in range(height):
        pixel_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:  # 黑点
                pixel_cnt_x += 1
        pixel_cnt_list.append(pixel_cnt_x)

    # 统计 30 列每列的黑点数
    for x in range(width):
        pixel_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:  # 黑点
                pixel_cnt_y += 1
        pixel_cnt_list.append(pixel_cnt_y)

    return pixel_cnt_list


import cv2
import numpy as np

from PIL import Image
from sklearn.externals import joblib

# ml model的位置
path_models = "../data/ml_models/"


def decode_vericode(img_cv2):
    # 获取特征，调用模型计算
    LR = joblib.load(path_models + "model_LR.m")

    img_gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)

    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # 返回三个值，图像，轮廓，轮廓的层析结构
    image, contours, hierarchy = cv2.findContours(img_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours_list = []

    # ii = 0,1,2,3
    for ii in range(len(contours)):
        contours_list.append(contours[3 - ii])

    # Store the decoded number
    num_decoded = ""

    # 外矩阵
    # cv2.boundingRect 计算轮廓的垂直边界最小矩形
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours_list[i])

        height = h
        width = w

        img_blank = np.zeros((30, 30, 3), np.uint8)

        # 生成一张新的空白背景的图像
        for ii1 in range(0, 30):
            for jj1 in range(0, 30):
                # img_cv2 [height高度][width宽度]
                img_blank[ii1][jj1] = (255, 255, 255)

        # 写入分割下来的数据
        for ii2 in range(0, height + 5):
            for jj2 in range(0, width + 5):
                # img_cv2 [height高度][width宽度]
                img_blank[ii2 + 5][jj2 + 5] = img_cv2[y + ii2][x + jj2]

        img_test = Image.fromarray(img_blank)

        features_single = get_features_single(img_test)
        predict_LR = LR.predict([features_single])
        num_decoded = num_decoded + str(predict_LR[0])

    print("Decoded number:", num_decoded)
    return num_decoded
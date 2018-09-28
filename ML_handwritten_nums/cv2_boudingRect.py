import cv2
import os
import numpy as np

path = "F:/code/python/P_web_spider/ecnu_vericodes/"

dir = os.listdir(path)
nums = len(dir)

for i in range(nums):
    img = cv2.imread(path + dir[i])
    print(i+1, dir[i])

    # 二值化
    img_gray = cv2.imread(path + dir[i], 0)

    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # 返回三个值，图像，轮廓，轮廓的层析结构
    image, contours, hierarchy = cv2.findContours(img_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("len(contours):", len(contours))
    contours_4 = []
    print("contours_4:", contours_4)

    # ii = 0,1,2,3
    for ii in range(len(contours)):
        contours_4.append(contours[3-ii])

    path_save = "F:/code/python/P_web_spider/single_nums/"


    # 外界矩阵
    # cv2.boundingRect 计算轮廓的垂直边界最小矩形
    for i1 in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours_4[i1])
        print("pos:", x, ",", y, '\t', x + w, ",", y + h)
        # img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        height = h
        width = w

        img_blank = np.zeros((30, 30, 3), np.uint8)

        # 生成一张新的空白背景的图像
        for ii1 in range(0, 30):
            for jj1 in range(0, 30):
                # img [height高度][width宽度]
                img_blank[ii1][jj1] = (255, 255, 255)

        # 写入分割下来的数据
        for ii2 in range(0, height + 5):
            for jj2 in range(0, width + 5):
                # img [height高度][width宽度]
                img_blank[ii2 + 5][jj2 + 5] = img[y + ii2][x + jj2]

        cv2.imwrite(path_save + "img_nums_" + str(i) + "_" + str(i1 + 1) + ".jpg", img_blank)

        print("dir:", path_save + "img_nums_" + str(i) + "_" + str(i1 + 1) + ".jpg")

    print('\n')

# for i2 in range(4):
#     img_blank = np.zeros(())

# cv2.imshow("img", img)
# cv2.waitKey(0)

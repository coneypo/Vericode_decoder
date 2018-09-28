import cv2
import numpy as np


def get_single_num():

    img = cv2.imread("../ML_handwritten_nums/saved_test.jpg")
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

    path_save_single_number = "../data/images/tmp_single_number/"

    # 外矩阵
    # cv2.boundingRect 计算轮廓的垂直边界最小矩形
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours_list[i])
        print("Number:", i+1)
        print("Position:(", x, ",", y, ')\t', "(", x + w, ",", y + h, ")")
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

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

        cv2.imwrite(path_save_single_number + "img_num_" + str(i + 1) + ".jpg", img_blank)

        print("Saved to:", path_save_single_number + "img_num_" + str(i + 1) + ".jpg")
        print('\n')
    print('\n')

    cv2.imshow("img", img)
    cv2.waitKey(0)


get_single_num()
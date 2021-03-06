# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

# 提取特征写入 CSV

from PIL import Image
import csv
import os

from reco_vericode import tools


# 遍历文件夹提取特征存入 CSV
def save_features_to_CSV():

    path_images = "../data/images/database_single_number/"
    path_csv = "../data/csvs/"

    sum_images = 0

    # 读取图像文件
    with open(path_csv+"tmp.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # 访问文件夹 1-9
        for i in range(1, 10):
            num_list = os.listdir(path_images + "num_" + str(i))
            print(path_images + "num_" + str(i))
            print("num_list:", num_list)
            # 读到图像文件
            if os.path.isdir(path_images + "num_" + str(i)):
                print("样本个数：", len(num_list))
                sum_images = sum_images + len(num_list)

                # Travsel every single image to generate the features
                for j in range(0, (len(num_list))):

                    # 处理读取单个图像文件提取特征
                    img = Image.open(path_images + "num_" + str(i)+"/" + num_list[j])
                    img = img.convert('1')
                    pixel_cnt_list = tools.get_features_single(img)
                    pixel_cnt_list.append(i)

                    # 写入 CSV
                    writer.writerow(pixel_cnt_list)
            print('\n')
        print("样本总数:", sum_images)


save_features_to_CSV()
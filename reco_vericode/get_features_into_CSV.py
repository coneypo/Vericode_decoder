# created at 2018-01-29
# updated at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/ML_handwritten_number

# 提取特征写入CSV

from PIL import Image
import csv
import os


# 提取单张图像的特征
def get_features_single(img):
    # 提取特征
    # 30*30 的图像
    pixel_cnt_list = []

    height, width = 30, 30

    # 统计30行每行的黑点数
    for y in range(height):
        pixel_cnt_x = 0
        for x in range(width):
            print(img.getpixel((x, y)))
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

# img = Image.open("/home/con/code/python/ML_handwritten_number/data/data_images/num_1/1_714.png")

img = Image.open("../data/images/database_single_number/num_0/img_nums_107_2.jpg")
print(img)
img = img.convert('L')

print(get_features_single(img))

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
                    pixel_cnt_list = []
                    pixel_cnt_list = get_features_single(img)
                    pixel_cnt_list.append(i)

                    # 写入 CSV
                    writer.writerow(pixel_cnt_list)
            print('\n')
        print("样本总数:", sum_images)


# save_features_to_CSV()
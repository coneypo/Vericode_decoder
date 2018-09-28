import os
from cv2_boundingRect_single import pic2fourparts

from PIL import Image
from sklearn.externals import joblib
from ML_handwritten_nums import get_features

path_test = "F:/code/python/P_web_spider/data/pics/for_test/pic_to_rename/"

# 1.将测试图片切割为四个图片
files = os.listdir(path_test)

for i in range(len(files)):
    pic2fourparts(path_test+files[i])

# 2.利用ML模型识别

    path_4_pics = "F:/code/python/P_web_spider/data/pics/single_pic_4_parts/"

    path_models = "F:/code/python/P_web_spider/ML_handwritten_nums/ml_models/"

    files4 = os.listdir(path_4_pics)

    nums_reco = []
    for ii in range(len(files4)):
        img = Image.open(path_4_pics+files4[ii])

        features_single = get_features.get_features_single(img)

        LR = joblib.load(path_models + "model_LR_1.m")

        predict_LR = LR.predict([features_single])

        nums_reco.append(int(predict_LR))

    new_name = (str(nums_reco[0])+str(nums_reco[1])+str(nums_reco[2])+str(nums_reco[3])+".jpg")

    os.rename(path_test+files[i], path_test+new_name)


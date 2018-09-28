# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# test_single_png.py
# 利用模型检测单张png的标记

from PIL import Image
from sklearn.externals import joblib
from get_features import get_features_single

path_test_pic = "F:/code/python/P_web_spider/data/pics/for_test/"

path_models = "F:/code/python/P_web_spider/ML_handwritten_nums/ml_models/"

img = Image.open(path_test_pic+"img_nums_29_4.jpg")

features_single = get_features_single(img)

print(features_single)

LR = joblib.load(path_models + "model_LR_1.m")

predict_LR = LR.predict([features_single])

print(predict_LR)

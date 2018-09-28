# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# test_single_png.py
# 利用模型检测单张png的标记

from PIL import Image

path_test_pic = "F:/code/python/P_web_spider/data/pics/for_test/"


img = Image.open(path_test_pic+"code_83.jpg")

#img.show()

# get features
import get_features
features_test_png = get_features.get_features_single(img)
print(features_test_png)

# ML ways
import ml_ways
ml_ways.pre_data()

ss_LR, LR = ml_ways.way_LR()
ss_LSVC, LSVC = ml_ways.way_LSVC()
ss_MLPC, MLPC = ml_ways.way_MLPC()
ss_SGDC, SGDC = ml_ways.way_SGDC()

X_test_single_LR = ss_LR.transform([features_test_png])
print("LR", '\t', LR.predict(X_test_single_LR))

X_test_single_LSVC = ss_LSVC.transform([features_test_png])
print("LSVC", '\t', LSVC.predict(X_test_single_LSVC))

X_test_single_MLPC = ss_MLPC.transform([features_test_png])
print("MLPC", '\t', MLPC.predict(X_test_single_LSVC))

X_test_single_SGDC = ss_SGDC.transform([features_test_png])
print("SGDC", '\t', SGDC.predict(X_test_single_SGDC))
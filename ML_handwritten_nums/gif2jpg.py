import numpy as np
import cv2
from PIL import Image

img_blank = np.zeros((60, 100, 3), np.uint8)

path_veri = "F:/code/python/P_web_spider/pics/"
img_veri = Image.open(path_veri+"vericode.jpg")

background = Image.new("RGB", img_veri.size, (255, 255, 255))
background.paste(img_veri)
background.save("saved_pic.jpg")
#img_veri.show()

print(background.format)

im_cv2 = cv2.imread("saved_pic.jpg")
print(im_cv2.shape)
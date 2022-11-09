import cv2
import numpy as np
import glob


for filename in glob.glob('*.png'):
    img = cv2.imread(filename, -1)                       # -1はAlphaを含んだ形式(0:グレー, 1:カラー)
    color_lower = np.array([0, 255, 0, 255])                 # 抽出する色の下限(BGR形式)
    color_upper = np.array([0, 255, 0, 255])                 # 抽出する色の上限(BGR形式)
    img_mask = cv2.inRange(img, color_lower, color_upper)    # 範囲からマスク画像を作成
    img_bool = cv2.bitwise_not(img, img, mask=img_mask)      # 元画像とマスク画像の演算(背景を白くする)
    img_resize = cv2.resize(img_bool, (1084,1125))
    output = "output/"+filename
    cv2.imwrite(output, img_resize)  
    print(output)                       # 画像保存

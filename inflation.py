import os
import cv2
import glob
from scipy import ndimage

# 画像を回転、ぼかし、閾値処理して水増しする

names = ["shiori", "rika", "mizuki", "sakura", "haruka"]
os.makedirs("./train", exist_ok=True)
for name in names:
    in_dir = "./face/"+name+"/*"
    out_dir = "./train/"+name
    os.makedirs(out_dir, exist_ok=True)
    in_jpg = glob.glob(in_dir)
    for i in range(len(in_jpg)):
        img = cv2.imread(str(in_jpg[i]))
        # 回転
        for ang in [-10,0,10]:
            img_rot = ndimage.rotate(img, ang)
            img_rot = cv2.resize(img_rot,(64,64))
            filename = os.path.join(out_dir, str(i) + "_" + str(ang) + ".jpg")
            cv2.imwrite(str(filename), img_rot)
            # 閾値
            img_thr = cv2.threshold(img_rot, 100, 255, cv2.THRESH_TOZERO)[1]
            filename = os.path.join(out_dir, str(i) + "_" + str(ang) + "thr.jpg")
            cv2.imwrite(str(filename), img_thr)
            # ぼかし
            img_fil = cv2.GaussianBlur(img_rot, (5, 5), 0)
            filename = os.path.join(out_dir, str(i) + "_" + str(ang) + "fil.jpg")
            cv2.imwrite(str(filename), img_fil)

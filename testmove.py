import shutil
import random
import glob
import os

names = ["shiori", "rika", "mizuki", "sakura", "haruka"]
os.makedirs("./test", exist_ok=True)


for name in names:
    in_dir = "./face/" + name + "/*"
    in_jpg=glob.glob(in_dir)
    random.shuffle(in_jpg)
    os.makedirs("./test/" + name, exist_ok=True)
    for t in range(len(in_jpg)//5):
        shutil.move(str(in_jpg[t]), "./test/"+name)

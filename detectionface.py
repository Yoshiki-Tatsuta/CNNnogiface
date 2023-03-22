import glob
import os
import cv2


names = ["shiori", "rika", "mizuki", "sakura", "haruka"]
out_dir = "./face"
os.makedirs(out_dir, exist_ok=True)

#元画像を取り出して顔部分を正方形で囲み、64×64pにリサイズ、別のファイルにどんどん入れてく
for i in range(len(names)):
    in_dir = "./data/"+names[i]+"/*.jpg"
    in_jpg = glob.glob(in_dir)
    os.makedirs(out_dir + "/" + names[i], exist_ok=True)
    print(len(in_jpg))
    for num in range(len(in_jpg)):
        image=cv2.imread(str(in_jpg[num]))
        if image is None:
            print("Not open:",num)
            continue
        
        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt.xml")
        # 顔認識の実行
        face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(64,64))
        #顔が１つ以上検出された時
        if len(face_list) > 0:
            for rect in face_list:
                x,y,width,height=rect
                image = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
                if image.shape[0]<64:
                    continue
                if image is not None and image.size != 0:
                    image = cv2.resize(image,(64,64))
                    #保存
                    filename=os.path.join(out_dir+"/"+names[i],str(num)+".jpg")
                    cv2.imwrite(str(filename),image)
                    print(str(num)+".jpgを保存しました。")
                else:
                    print("画像のサイズがゼロです")
        #顔が検出されなかった場合
        else:
            print("顔が見つかりません…ぴえん")
            continue
        print(image.shape)

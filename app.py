from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
import os
import numpy as np
import cv2
from datetime import datetime
from keras.models import load_model
import shutil
import glob
import matplotlib.pyplot as plt
from japanize_matplotlib import japanize_matplotlib
japanize_matplotlib.japanize()

app = Flask(__name__)

# 画像の読み込み
savepath = "static/save_images/"

# モデルを読み込む
my_model = load_model("mybestmodel.h5")

# home.html
@app.route("/")
def home():
    return render_template("home.html")

# image.html
@app.route("/image", methods = ["GET", "POST"])
def image():
    
    if request.method == "GET":
        return render_template("image.html")
    
    elif request.method == "POST":
        
        # 保存先の作成
        if os.path.exists(savepath):
            shutil.rmtree(savepath)
        os.makedirs(savepath)
        
        # 画像の取得
        input_image = request.files["input_image"]
        
        # stream形式で読み取る
        stream_image = input_image.stream.read()
        array_image = np.array(bytearray(stream_image))
        show_image = cv2.imdecode(array_image, cv2.IMREAD_COLOR)
        
        # 画像の保存
        date_now = datetime.now().strftime("%Y%m%d-%H%M%S")
        savefile_nmae = savepath + date_now + ".jpg"
        print(f"画像の保存先の確認：{savefile_nmae}") # ターミナルで画像を保存する先を確認するために表示
        cv2.imwrite(filename = savefile_nmae, img = show_image)
        
        return render_template("image.html", image_path = savefile_nmae)

# result.html
@app.route("/result", methods = ["GET"])
def result():
    
    # パスの取得
    filepath = glob.glob(savepath + "*.jpg")
    img_path = filepath[0]
    print(img_path)
    
    # 画像の加工
    img_array = cv2.imread(filename = img_path, flags=cv2.IMREAD_COLOR)
    img_array_resize = cv2.resize(src=img_array, dsize=(64, 64))
    img_bgr2rgb = cv2.cvtColor(img_array_resize, cv2.COLOR_BGR2RGB)

    # 結果
    img = np.array([img_bgr2rgb]) # モデルが学習できるように次元を上げて(1, 64, 64, 3)にする
    pred = my_model.predict(img)
    predict_label = int(np.argmax(pred, axis=1))
    
    if predict_label == 0:
        result_label = "ネコ"
    else:
        result_label = "イヌ"
        
    # 棒グラフの結果を作成
    plt.figure(figsize=(12, 7))
    plt.barh(y = [0, 1], width = pred.reshape(-1))
    plt.yticks(ticks = [0, 1], labels = ["ネコ", "イヌ"])
    plt.xticks(ticks=np.arange(0, 1.1, 0.1))
    plt.ylabel("クラス", size = 20)
    plt.xlabel("精度", size = 20)
    plt.tick_params(axis = "both", which = "major", labelsize = 18)
    # 結果の保存
    fig_path = savepath + "result.png"
    plt.savefig(fig_path)
    
    return render_template("result.html"
                        , result_label = result_label
                        , result_img = img_path
                        , result_fig = fig_path)

if __name__ == "__main__":
    app.run(debug = True)

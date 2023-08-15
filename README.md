# 注意事項
このアプリはVScode上で実行することを前提としています。  
実行する前に、VScode上で下記⓵～⓷を行ってください。  
  
- **⓵ VScode上のターミナルで仮想環境を構築する。**  
- **⓶ 仮想環境をアクティブにする。**  
- **⓷ requirements.txtをインストールする。**  
  
下記は先の一連のコードです。下記のコードをターミナル上でおこなってください。  

""""  
C:\Users\user1\sample1> python -m venv env  
C:\Users\user1\sample1> env\Scripts\activate  
(env) C:\Users\user1\sample1> python -m pip install -r requirements.txt  
""""  

仮想環境がアクティブになると、C:\Users\user1\sample1> が (env) C:\Users\user1\sample1>になります。

# first_app
## 概要
転移学習という技術を使い、イヌとネコを判別する画像認識AIを作成しました。  
Flaskを用いて、そのAIをローカルのPC上で動かせるようにしました。  
初めて作成したアプリケーションです。  

## 目的
⓵：pythonを使ってwebアプリケーションを作成すること。  
⓶：作ったAIをwebアプリとして使えるような形にすること。  
  
## 起動のさせ方
VScodeを起動させる。  
⓵：「注意事項」の「requirements.txtをインストールする。」までを行う。  
⓶：下記のようにターミナル上で「python app.py」を入力する。  
"""  
(env) C:\Users\user1\sample1> python app.py  
"""  
⓷：⓶の後、下記のような表示が出てくるので、URLをクリックすると使用できる。  
  
""""  
Serving Flask app 'app'  
Debug mode: on  
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.  
Running on *URL*  
Press CTRL+C to quit  
Restarting with stat  
""""  
  
⓸終了する際は、表示されたブラウザを閉じ、VScodeのターミナル上でCTRL+Cをクリックする。

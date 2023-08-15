# このアプリを動かす前に絶対読んでください
このアプリはVScode上で動かすことを前提としています。  
動かす前に、下記の順番で入力してください。  
  
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
イヌと猫を判別するAIを転移学習を使い作成しました。  
そのAIをローカルのPC上で動かせるようにした初めてアプリケーションです。
  
「どうやったらPC上で使えるようになるのかを記載する」  
VScodeを起動させる  
⓵：仮想環境に入るためにターミナル上で env\Scripts\activate を入力  
⓶：下記のようにターミナル上で「python app.py」を入力  
"""  
(env) C:\Users\user1\sample1> python app.py  
"""  
⓷：⓶の後、下記のような表示が出てくるので、URLをクリックすると使用できる  
  
""""  
Serving Flask app 'app'  
Debug mode: on  
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.  
Running on *URL*  
Press CTRL+C to quit  
Restarting with stat  
""""  
  
⓸終了する際は、表示されたブラウザを閉じ、VScodeのターミナル上でCTRL+Cをクリックする。

# first_app
イヌと猫を判別するAIを転移学習を使い作成しました。  
そのAIをローカルのPC上で動かせるようにした初めてアプリケーションです。
  
「どうやったらPC上で使えるようになるのかを記載する」  
VScodeを起動させる  
⓵：仮想環境に入るためにターミナル上で env\Scripts\activate を入力  
⓶：ターミナル上で「python app.py」を入力  
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

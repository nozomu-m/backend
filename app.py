# -*- coding: utf-8 -*-
# 日本語を使う場合は絶対に必要

# flaskなどの必要なライブラリをインポート
import os
import datetime
from flask import Flask
from flask import jsonify

# 自分の名称を app という名前でインスタンス化
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "OK", "Date": datetime.datetime.now()})

if __name__ == '__main__':
    app.run()

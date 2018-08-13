# -*- coding: utf-8 -*-
# 日本語を使う場合は絶対に必要

import datetime
# flaskなどの必要なライブラリをインポート
import os
import time

from flask import Flask
from flask import jsonify
from flask_cors import CORS

# 自分の名称を app という名前でインスタンス化
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({"status": "OK", "Date": datetime.datetime.now()})


@app.route('/unixtime')
def unixtime():
    return jsonify({"status": "OK", "UnixTime": time.time()})


if __name__ == '__main__':
    app.run()

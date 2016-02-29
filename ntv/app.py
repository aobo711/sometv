# coding: utf-8

from datetime import datetime

import hashlib

from flask import Flask, request
from flask import render_template

from views.todos import todos_view

app = Flask(__name__)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return str(datetime.now())


@app.route('/verify')
def verify():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')

    token = 'yZh6WUBTKk8ZeC'

    temp = []
    temp.append(token)
    temp.append(str(timestamp))
    temp.append(str(nonce))
    temp.sort()
    
    out = hashlib.sha1(''.join(temp))

    if out.hexdigest() == signature:
        return echostr
    else:
        return 'U get lost.'


#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/signin_form',methods = ['Get','POST'])
def signin_form():
    return render_template('signform.html')
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    userlist=['Richie','Ann','Dan']
    if username=='admin' and request.form['password'] == 'password':
        return render_template('sign_ok.html',username=username,userlist=userlist)
    else:
        return render_template('signform.html',message='Bad username or password!')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
    # app.run()

#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import model
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.ftl')

@app.route('/login/',methods=['post'])
def login():
    username = request.form.get('username','')
    password = request.form.get('password','')
    if model.validate_user_login(username,password):
        return redirect('/users/')
    else:
        return render_template('index.ftl',loginerr="登录失败,用户名或密码错误",\
                               loginusername=username,\
                               loginpassword=password)

@app.route('/register/',methods=['post'])
def register():
    username = request.form.get('username','')
    password = request.form.get('password','')
    age=request.form.get('age','')
    telephone=request.form.get('telephone','')
    status,msg = model.validate_user_add(username,password,age,telephone)
    if status:
        model.add_user(username,password,age,telephone)
        msg="注册成功"
        return render_template('index.ftl',\
                               registerstatus=status,\
                               registermsg=msg)
    else:
        return render_template('index.ftl',\
                               registerstatus=status,\
                               registermsg=msg,\
                               username=username,\
                               age=age,\
                               telephone=telephone)

@app.route('/users/')
def users():
    users = model.get_user()
    return render_template('users.ftl',users=users)
    






    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)

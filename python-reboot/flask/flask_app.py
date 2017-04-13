#encoding:utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return "hello world"

@app.route('/printname')
def print_args():
    return "hello %s"%request.args.get('name')

@app.route('/login')
def login():
    name = request.args.get('name')
    return render_template('login.ftl',name=name)

@app.route('/register')
def register():
    return render_template('register.ftl')

@app.route('/validate',methods=['GET','POST'])
def loginvalidate():
    if request.method == 'GET':
        name = request.args.get('username')
        password = request.args.get('password')
    else:
        name = request.form.get('username')
        password = request.form.get('password')
    f=open('db.txt')
    userinfo_dict = {}
    userinfo_list = f.readlines()
    f.close()  
    for userinfo in userinfo_list:
        if userinfo.strip == '':
            break
        userinfo=userinfo.split(':')
        _userinfo_name=userinfo[0]
        _userinfo_password=userinfo[1]
        userinfo_dict[_userinfo_name]=_userinfo_password
  
    if name in userinfo_dict and password == userinfo_dict.get(name):
        return redirect('/login_succ')
    else:
        return render_template('login.ftl',error="login faild!")


@app.route('/login_succ')
def login_succ():
    logs=[('192.168.1.2','4','404','/'),
          ('192.168.1.13','5','404','/url'),
          ('192.168.1.12','3','404','/r'),
          ('192.168.1.14','7','200','/test'),
          ('192.168.1.16','2','404','/success'),
          ('192.168.1.51','8','200','/faild')
          ]
    return render_template('logs.ftl',logs=logs)


@app.route('/registerdate',methods=['POST'])
def registerdate():
    name = request.form.get('username')
    password = request.form.get('password')
    phonenum = request.form.get('phonenum')
    f=open('db.txt','a+')
    userinfo=f.read()
    if name in userinfo:
        return 'user already exsit'
    else:
        reginfo=name+':'+password+":"+phonenum+'\n'
        f.write(reginfo)
    f.close()
    return 'success'
    











if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)

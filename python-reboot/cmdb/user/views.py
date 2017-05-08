#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
from functools import wraps

# 引入flask中的必要类和函数
from flask import Flask              #创建Flask APP对象
from flask import request            #用于获取用户提交的数据
from flask import render_template    #加载模板
from flask import redirect           #重定向到其他url
from flask import session 

# 导入自定义的模块
import models

# 创建一个Flask app
# Flask需要根据传递的参数去寻找templates, static等目录的位置
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX aHH!sajmN]LWX/,?RT'

# 登录验证装饰器
def login_required(func):
    @wraps(func)
    def wapper(*args,**kwargs):
        if session.get('user') is None:
            return redirect('/')
        rtn = func(*args,**kwargs)
        return rtn
    return wapper

# homepage
# 定义路由, 如果以GET方式访问url地址为/则由index函数处理
@app.route('/')
def index():
    #print 'i am /'
    # 返回templates目录下的login.html模板中的内容
    return render_template('login.html')

# 登陆验证
# 定义路由, 若以GET、POST方式提交请求到url地址/login/则有login函数处理
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # 如果为GET请求则从request.args中获取提交的数据
    # 如果为POST请求则从request.form中获取提交的数据
    params = request.args if request.method == 'GET' else request.form
    
    # 获取username和password信息
    username = params.get('username', '')
    password = params.get('password', '')
    
    # 验证用户名和密码
    if models.validate_user_login(username, password):
        session['user']=username
        # 成功则显示所有用户的信息列表
        return redirect('/users/')
    else:
        # 失败则提示用户失败, 依然返回登陆页面
        return render_template('login.html', error='用户名或密码错误', login_username=username)

'''
# 注册功能不提供
# 注册
# 定义路由, 若以POST方式提交请求到url地址/register/则有register函数处理
@app.route('/register/', methods=['POST'])
def register():
    # 从request.form中获取username、password、telephone信息
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    telephone = request.form.get('telephone', '')
    age = request.form.get('age', '')

    # 检查用户提交的数据
    ok, result = models.validate_user_add(username, password, telephone, age)
    
    # 如果检查通过则添加到文件中
    if ok:
        if models.add_user(username, password, telephone, age):
            ok = True
            result = '注册成功'
        else:
            ok = False
            result = '注册失败'

    return render_template('login.html', ok=ok, result=result, register_username=username, password=password, telephone=telephone, age=age)
'''

# 获取用户列表
# 定义路由, 如果以GET方式访问url地址为/users/则由users函数处理
@app.route('/users/', methods=['GET', 'POST'])
@login_required
def users():
    params = request.args if request.method == 'GET' else request.form
    _query = params.get('query', '')
    # 获取所有用户
    _users = models.get_users(_query)
    #print "iam users"
    # 返回用户列表页面
    #print session.get('user')
    #print _users
    return render_template('users.html', users=_users, query=_query)

'''
# 改到dialog
# 添加用户信息(打开页面)
@app.route('/createUser/')
@login_required
def createUser():
    return render_template('create.html')
'''

# 添加用户信息(更新DB)
@app.route('/addUser/', methods=['POST'])
@login_required
def addUser():
    # 从request.form中获取username、password、telephone信息
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    telephone = request.form.get('telephone', '')
    age = request.form.get('age', '')

    # 检查用户提交的数据
    ok, result = models.validate_user_add(username, password, telephone, age)
    
    # 如果检查通过则添加到文件中
    if ok:
        if models.add_user(username, password, telephone, age):
            ok = True
            result = '添加成功'
        else:
            ok = False
            result = '添加失败'
    '''        
    if ok:
        return redirect('/users/')
    
    else:
        return render_template('create.html',  result=result, register_username=username, password=password, telephone=telephone, age=age)
    '''
    return json.dumps({'ok':ok,'result':result})

'''
# 改到dialog
# 更新用户信息(打开页面)
@app.route('/modifyUser/')
@login_required
def modifyUser():
    _id = request.args.get('id', '')
    _user = models.get_user_by_id(_id)
    if _user is None:
        return render_template('update.html', result='用户信息不存在')
    else:
        return render_template('update.html', id=_user['id'], username=_user['username'], telephone=_user['telephone'], age=_user['age'])
'''

# 更新用户信息(更新DB)
@app.route('/updateUser/', methods=['POST','GET'])
@login_required
def updateUser():
    _id = request.form.get('id', '')
    _user = models.get_user_by_id(_id)
    if _user is None:
        #return render_template('update.html', result='用户信息不存在')
        ok,result = False,'用户信息不存在'
    else:
        telephone = request.form.get('telephone', '')
        age = request.form.get('age', '')

        # 检查用户提交的数据
        ok, result = models.validate_user_modify(telephone, age)
        # 如果检查通过则添加到DB
        if ok:
            if models.modify_user(_user['id'], telephone, age):
                ok = True
                result = '更新成功'
            else:
                ok = False
                result = '更新失败'
        '''
        if ok:
            #return redirect('/users/')
            print 'here1'
            return json.dumps({'ok':True})
        else:
            print 'here2'
            return json.dumps({'ok':False,'result':result})
            #return render_template('update.html', result=result, id=_user['id'], username=_user['username'], telephone=telephone, age=age)
        '''
    return json.dumps({'ok':ok,'result':result})

# 删除用户信息
@app.route('/deleteUser/')
@login_required
def deleteUser():
    _id = request.args.get('id', '')
    ok,result = models.delete_user(_id)
    if not ok:
        result = "用户删除失败"
    #return redirect('/users/')
    return json.dumps({'ok':ok,'result':result})


# 注销登录
@app.route('/logout/')
def logout():
    session.pop('user')
    return redirect('/users/')

# 资产管理
@app.route('/assets/', methods=['GET', 'POST'])
@login_required
def assets():
    params = request.args if request.method == 'GET' else request.form
    _query = params.get('query', '')
    _assets = models.get_assets(_query)
    #print "iam users"
    #print _assets
    return render_template('assets.html', assets=_assets, query=_query)





# 机房列表
@app.route('/machine_rooms/', methods=['GET', 'POST'])
@login_required
def machine_rooms():
    _machine_rooms = models.get_machine_rooms()
    #print "views"
    #print _machine_rooms
    #print json.dumps(_machine_rooms)
    #print json.dumps({1:'上海',2:'北京'})
    #print json.dumps(dict([ (_value[0],_value[1]) for _value in _machine_rooms]))
    #return json.dumps(dict([(_value[0],_value[1]) for _value in _machine_rooms]))
    return json.dumps(_machine_rooms)


# 新增资产
@app.route('/addAsset/', methods=['POST'])
@login_required
def addAsset():
    print request.form
    sn = request.form.get('sn','')
    ip = request.form.get('ip','')
    hostname = request.form.get('hostname','')
    machine_room_id = request.form.get('machine_room','')
    cpu = request.form.get('cpu','')
    purchase_date = request.form.get('purchase_date','')

    ok, result = models.validate_asset_add(sn,ip,hostname,machine_room_id,cpu,purchase_date)
    
    if ok:
        if models.add_asset(sn,ip,hostname,machine_room_id,cpu,purchase_date):
            ok = True
            result = '添加成功'
        else:
            ok = False
            result = '添加失败'
    
    return json.dumps({'ok':ok,'result':result})









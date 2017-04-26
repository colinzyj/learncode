#encoding:utf-8
import dbutil


# 验证用户名密码
def validate_user_login(username,password):
    _rt_cnt,_rt_fetch=dbutil.execute_sql('select * from user where username=%s and password =md5(%s)',(username,password),is_fetch=True)
    return _rt_cnt != 0

# 验证注册信息
def validate_user_add(username,password,age,telephone):
    #print age
    #print type(age)
    #print age.isdigit()
    if username == '' or password == '':
        return False,'用户名或密码不能为空'
    elif age != '' and not age.isdigit() :
        return False,'年龄必须是数字'
    else:
        _rt_cnt,_rt_fetch=dbutil.execute_sql('select * from user where username=%s',(username,),is_fetch=True)
        if _rt_cnt != 0:
            return False,'用户名已经存在'
        else:
            return True,''

# 用户注册
def add_user(username,password,age,telephone):
    _rt_cnt,_rt_fetch=dbutil.execute_sql('insert into user(username,password,age,telephone)\
                        values(%s,md5(%s),%s,%s)',\
                        (username,password,age,telephone))


# 获取用户信息
def get_user():
    _rt_cnt,_rt_fetch=dbutil.execute_sql('select username,age,status from user',is_fetch=True)
    return _rt_fetch



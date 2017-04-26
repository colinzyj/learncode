#encoding:utf-8
import MySQLdb
import gconf

# @method 执行sql
# @param str sql 需要执行的sql语句
# @param tuple args 预定义的变量，默认为空元组
# @param boolean is_fetch 是否为查询语句，默认为False 

def execute_sql(sql,args=(),is_fetch=False):
    _conn,_cur = None,None
    _rt_cnt,_rt_fetch=0,()
    try:
        _conn = MySQLdb.connect(host=gconf.DB_HOST,\
                    port=gconf.DB_PORT,\
                    user=gconf.DB_USER,\
                    passwd=gconf.DB_PASS,\
                    db=gconf.DB_NAME,\
                    charset=gconf.DB_CHARSET)
        _cur = _conn.cursor()
        _rt_cnt = _cur.execute(sql,args)
        if is_fetch:
            _rt_fetch = _cur.fetchall()
        else:
            _conn.commit()
    except BaseException,e:
        print e
    finally:
        if _cur is not None:
            _cur.close()
        if _conn is not None:
            _conn.close()

    return _rt_cnt,_rt_fetch


if __name__ == '__main__':
    # 用户添加
    print execute_sql('INSERT INTO users(name, password) VALUES(%s, md5(%s));', ('kk', '123456'))
    # 验证用户登录
    
    print execute_sql('SELECT * FROM users WHERE name=%s AND password=md5(%s);', ('kk', '123456'), True)
    '''
    # 更改用户密码
    print execute_sql('UPDATE users SET password=md5(%s) WHERE name=%s;', ('123456789', 'kk'))
    # 验证用户登录
    print execute_sql('SELECT * FROM users WHERE name=%s AND password=md5(%s);', ('kk', '123456'), True)
    # 删除用户
    print execute_sql('DELETE FROM users where name=%s', ('kk',))
    
    # 添加10个用户
    for i in range(10):
        execute_sql('INSERT INTO user(name, password) VALUES(%s, md5(%s));', ('kk_%s' % i, '123456'))
    
    # 查询所有用户
    _cnt, _rt = execute_sql('SELECT * FROM user', (), True)
    print _cnt
    # 遍历所有用户
    for _rs in _rt:
        print _rs

    # 删除所有用户
    print execute_sql('DELETE FROM user')

    # 获取用户数量
    print execute_sql(sql='SELECT count(*) FROM user', is_fetch=True)
    '''

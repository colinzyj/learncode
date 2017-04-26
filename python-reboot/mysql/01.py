#encoding:utf-8

import MySQLdb

host='172.18.0.73'
port = 3306
user = 'zyj'
passwd = '123456'
db = 'name'
charset = 'utf8'

#连接数据库
conn = MySQLdb.Connect(host=host,port=port,user=user,\
                       passwd=passwd,db=db,charset=charset)

#获取游标
cur = conn.cursor()

#增、改、删
#cur.execute('insert into user(name) values("colin2")')
#cur.execute('update user set name="zyj" where id = 5')
#cur.execute('delete from user where id = 6')
#conn.commit()

#回退
#conn.rollback()

#查
#cur.execute('select * from user')
#cur.fetchone()
#cur.fetchall()

#关闭游标
#cur.close()
#关闭连接
#conn.close()

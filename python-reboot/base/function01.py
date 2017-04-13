#encoding:utf-8

def jiechen(num):
    _result=1
    for n in range(num,0,-1):
        _result = _result * n
    return _result

'''
while True:
    print '的阶乘是'
    txt=raw_input('请输入一个数字阶乘：')
    if txt == 'quit':
        break
    try:
        _n = int(txt)
        print '%s的阶乘%s'%(_n,jiechen(_n))
        print '的'
    except:
        print '请输入一个数字'

'''


   
def print_name(name,age):
    '''
    print user
    '''
    print '你的名字是:%s,你的年龄是:%s'%(name,age)

#print_name('c',17)
#print_name(age=17,name='a')
#help(print_name)


def print_user(name,age,sex=1):
    if sex ==1:
        _sex='男'
    else:
        _sex='女'
    print 'name:%s,age:%s,sex:%s'%(name,age,_sex)

#print_user('cobe',17)
#print_user('anbe',17,2)


def p_cs2(*args,**arge2):
	print args
	print arge2

#p_cs2(1,2,3,4,abc=1,d=3)


def add_all(*args):
    _sum=0
    for _num in args:
        if isinstance(_num,int):
            _sum += _num
        else:
            continue
    return _sum

print add_all(1,2,3,4,5)
    













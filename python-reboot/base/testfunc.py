# encoding:utf-8
def deco_functionNeedDoc(func):
    if func.__doc__ == None :
        print func, "has no __doc__, it's a bad habit."
    else:
        print func, ':', func.__doc__, '.'
    return func
@deco_functionNeedDoc
def f():
    print 'f() Do something'
@deco_functionNeedDoc
def g():
    'I have a __doc__'
    print 'g() Do something'
f()
g()


def permit_require(permitid):
    def __perm(func):
        @wraps(func)
        def __wapper(*args, **kwargs):
            # permitlist,从数据库中获取的权限值
            # permitlist = models.Permit.getbykey(uid=session.get('user'))
            permitlist = ['20010', '20011']
            if permitid in permitlist:
                rtn = func(*args, **kwargs)
            else:
                abort(403)
            # return redirect('/')
            return rtn
        return __wapper
    return __perm

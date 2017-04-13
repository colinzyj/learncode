#encoding:utf-8
'''
try:
    print 4/0
except ZeroDivisionError as e:
    print e
    print e.args
    print e.message
'''

try:
    #raise ZeroDivisionError('abc')
    print 4/2
except ZeroDivisionError as e:
    print 'zero',e
except BaseException as e:
    print 'baseexception',e.args

finally:
    print 'finelly'


    

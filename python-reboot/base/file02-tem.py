#encoding:utf-8
fpath='tem.txt'

f=open(fpath,'r')

max_tem=None
total_tem=0
cnt_tem=0

max_tem2=None
total_tem2=0
cnt_tem2=0

l3=[]

for _line in f:

    # ff1
    _date,_tem=_line.split()
    _tem=int(_tem)
    _y,_m,_d=_date.split('-')
    _y=int(_y)
    _m=int(_m)
    _d=int(_d)

    if _y==2015 and _m == 1 and _d >=1 and _d <=10:
        total_tem += _tem
        cnt_tem +=1
        if _tem > max_tem:
            max_tem = _tem
    # ff2
    _date2,_tem2=_line.split()
    if _date2.startswith('2015-01-0') or _date2.startswith('2015-01-10'):
        _tem2 = int(_tem2)
        #
        total_tem2 += _tem2
        cnt_tem2 += 1
        if _tem2 > max_tem2:
            max_tem2 = _tem2
        #
        l3.append(_tem2)



print '第一次：计数值：%d,总计值：%d,最大值：%d,平均温度：%f'%(cnt_tem,total_tem,max_tem,total_tem*1.00/cnt_tem)
print '第二次：计数值：%d,总计值：%d,最大值：%d,平均温度：%f'%(cnt_tem2,total_tem2,max_tem2,total_tem2*1.00/cnt_tem2)
print '第三次：计数值：%d,总计值：%d,最大值：%d,平均温度：%f'%(len(l3),sum(l3),max(l3),sum(l3)*1.00/len(l3))

f.close()

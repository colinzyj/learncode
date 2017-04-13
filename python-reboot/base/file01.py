#encoding:utf-8

fpath="test.txt"
f=open(fpath,'r+')
line_idx=0
r_list=[]
for _line in f:
    line_idx+=1
    if line_idx==2:
        _line='wd'
    else:
        _line=_line.replace('reboot','hello').strip('\n')
    r_list.append(_line)

f2=open('test2.txt','w')

f2.writelines(r_list)
f.close()
f2.close()

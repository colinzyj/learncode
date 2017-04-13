#encoding:utf-8

num_list=[9,2,3,7,4,5,6]
num_list2=[9,2,3,7,4,5,6]
#num_list.reverse()
#num_list2.reverse()

def charu(num_list):
    len_list=len(num_list)
    x_cnt=0       #统计比较计算的次数
    for i in range(1,len_list):
        for x in range(i,0,-1):
            x_cnt+=1
            if num_list[x] < num_list[x-1]:                
                num_list[x],num_list[x-1] = num_list[x-1],num_list[x]
            else:
                break
    print num_list,x_cnt

def maopao(mylist):
    x_cnt=0
    for i in range(1,len(mylist)):
        for n in range(len(mylist)-i):
            x_cnt+=1
            if mylist[n] > mylist[n+1]:
                mylist[n],mylist[n+1]=mylist[n+1],mylist[n]
    print mylist,x_cnt


charu(num_list)
maopao(num_list2)

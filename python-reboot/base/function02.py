#encoding:utf-8

#v1
mylist=[('a',3),('g',1),('b',7),('x',5),('u',93),('p',2)]
def my_sort(mylist):
    for i in range(1,len(mylist)):
        for n in range(len(mylist)-i):
            if mylist[n] > mylist[n+1]:
                mylist[n],mylist[n+1]=mylist[n+1],mylist[n]
my_sort(mylist)
print mylist

#v2
mylist2=[('a',3),('g',1),('b',7),('x',5),('u',93),('p',2)]
def my_sort2(mylist):
    for i in range(1,len(mylist)):
        for n in range(len(mylist)-i):
            if mylist[n][1] > mylist[n+1][1]:
                mylist[n],mylist[n+1]=mylist[n+1],mylist[n]
my_sort2(mylist2)
print mylist2


#v3
mylist3=[('a',3),('g',1),('b',7),('x',5),('u',93),('p',2)]
def my_sort_key(e):
    return e
def my_cmp_key(x,y):
    return x > y
def my_sort3(mylist,sort_key=None,sort_cmp=None):
    if sort_key is None:
        sort_key = my_sort_key
    if sort_cmp is None:
        sort_cmp = my_cmp_key
    for i in range(1,len(mylist)):
        for n in range(len(mylist)-i):
            if sort_cmp(sort_key(mylist[n]),sort_key(mylist[n+1])):
                mylist[n],mylist[n+1]=mylist[n+1],mylist[n]
my_sort3(mylist3,sort_key=lambda x:x[1])
print mylist3






















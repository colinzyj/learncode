#encoding:utf-8
'''
s1='reboot'

sn=''
sl=[]
for i in s1:
    sn = i+sn
    sl.insert(0,i)


sl=''.join(sl)
'''
'''
s1 = 'user1:119,user2:112,user3:113'
l1=[]
for s in s1.split(','):
    l1.append(tuple(s.split(':')))
print l1
'''
read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
#read_me='abcdjlklcval;weqr'
char_stat_dict={}
for _char in read_me:
    char_stat_dict.setdefault(_char,0)
    char_stat_dict[_char]+=1
'''
char_stat_list=char_stat_dict.items()

for _num in range(len(char_stat_list)):
    for i in range(len(char_stat_list)- _num -1):
        if char_stat_list[i][1] > char_stat_list[i+1][1]:
            char_stat_list[i],char_stat_list[i+1]=char_stat_list[i+1],char_stat_list[i]
print char_stat_list[:-11:-1]            

for x,y in char_stat_list:
    print '\"{x}\"'.format(x=x)
''' 

new_char_stat_dict={}
for _key,_value in char_stat_dict.items():
    new_char_stat_dict.setdefault(_value,[])
    new_char_stat_dict[_value].append(_key)

print new_char_stat_dict


char_num_list=new_char_stat_dict.keys()
char_num_list.sort(reverse=True)
print char_num_list
cnt_num=0
cnt_total=10

for _num in char_num_list:
    _value=new_char_stat_dict[_num]
    print _value
    #value排序
    _value.sort()
    print _value
    for _char in _value:
        print _char
        cnt_num +=1
        if cnt_num >= cnt_total:
            break
    if cnt_num >= cnt_total:
            break

        















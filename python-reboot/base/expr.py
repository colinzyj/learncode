#encoding:utf-8


#分割字符串表达式
def split_expr(expr):
    expr_list=[]
    num_str=''
    for i in expr:
        if i not in '+-*/':
            num_str+=i
        else:
            expr_list.append(float(num_str))
            num_str=''
            expr_list.append(i)
    if num_str != '':
        expr_list.append(float(num_str))
    return expr_list

def num_cal(op,left_num,right_num):
    if op == '+':
        return left_num + right_num
    elif op == '-':
        return left_num - right_num
    elif op == '*':
        return left_num * right_num
    elif op == '/':
        return left_num / right_num
    else:
        raise ValueError
    
def expr_calc(expr_list):
    left_num = expr_list[0]
    step = 2
    for i in range(1,len(expr_list),step):
        op = expr_list[i]
        right_num = expr_list[i+1]
        left_num = num_cal(op,left_num,right_num)
    return left_num
    
def expr_calc2(expr_list):
    #复制一个list
    n_expr_list=expr_list[:]
    
    while '*' in n_expr_list:
        _op_index = n_expr_list.index('*')
        n_expr_list[_op_index-1:_op_index+2]= \
        [num_cal('*',n_expr_list[_op_index-1],n_expr_list[_op_index+1])]
    while '/' in n_expr_list:
        _op_index = n_expr_list.index('/')
        n_expr_list[_op_index-1:_op_index+2]= \
        [num_cal('/',n_expr_list[_op_index-1],n_expr_list[_op_index+1])]

    left_num = n_expr_list[0]
    step = 2
    for i in range(1,len(n_expr_list),step):
        op = n_expr_list[i]
        right_num = n_expr_list[i+1]
        left_num = num_cal(op,left_num,right_num)
    print expr_list
    print n_expr_list
    return left_num


if __name__ == '__main__':
    expr_str='12+2*3/2-5'
    print split_expr(expr_str)
    print num_cal('/',10,6)
    print expr_calc2(split_expr(expr_str))


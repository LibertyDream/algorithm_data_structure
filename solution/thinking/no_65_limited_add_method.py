'''面试题65：不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用“+”、“-”、“x”、“+”四则运算符号
'''

def limited_add(a_num,b_num):

    if not isinstance(a_num,int) or not isinstance(b_num,int):
        return None
    
    while b_num != 0:
        add = a_num ^ b_num
        carray = (a_num & b_num) << 1
        a_num = add
        b_num = carray

    return a_num

if __name__ == "__main__":

    datas = [[1,2],[3,-4],[None,None]]

    for data in datas:
        print(data,limited_add(*data))
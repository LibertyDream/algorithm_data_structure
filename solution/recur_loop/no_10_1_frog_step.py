'''题目二：青蛙跳台阶问题。

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

def frog_step(n):

    if n < 1 or n is None:
        return

    f_1 = 1
    f_2 = 2
    ret = 0
    if n == 1:
        ret = f_1
    elif n == 2:
        ret = f_2
    else:
        for i in range(3, n):
            ret = f_2 + f_1
            f_1 = f_2
            f_2 = ret
    return ret
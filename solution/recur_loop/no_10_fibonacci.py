'''面试题10-1：斐波那契数列

求斐波那契数列的第n项。写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。
'''

def Fibonacci(n):

    if n < 1 or n is None:
        return
    
    goal = 0
    f_1 = 0
    f_2 = 1
    if n == 1:
        goal = f_1
    else:
        for i in range(2, n):
            goal = f_1 + f_2
            f_1 = f_2
            f_2 = goal
    
    return goal

if __name__ == "__main__":

    # 0 1 1 2 3 5 8 13 21
    print(Fibonacci(6))
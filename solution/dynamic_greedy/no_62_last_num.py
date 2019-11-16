'''面试题62：圆圈中最后剩下的数字

0,1,...,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字
--------------
f(n,m) = (f(n-1,m)+m) % n, f(1) = 0
'''

def last_num(n, m):

    if n is None or m is None or n < 1 or m < 1:
        return -1

    last = 0

    for i in range(2, n+1):
        last = (last + m) % i

    return last

if __name__ == "__main__":

    datas = [[1,3],[5,3],[-1,3],[2,None]]

    for data in datas:
        print(last_num(*data))
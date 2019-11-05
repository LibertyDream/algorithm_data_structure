'''面试题15-1：二进制中1的个数

请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。
---------------
Example
input: 9  # 1001
output: 2
--------------------
1. 除法效率远没有移位运算效率高，尽量使用移位运算
2. 把一个整数减去1之后再和原来的整数做位与运算，
得到的结果相当于把整数的二进制表示中最右边的1变成0。
'''

def bin_nums_of_1(num):
    
    if not isinstance(num, int):
        return -1

    count = 0
    while num != 0:
       num = num & (num - 1)
       count += 1
    return count

if __name__ == "__main__":
    print('num,binary,nums_of_1')
    for num in range(20):
        print("%d, %s, %d" % (num, bin(num), bin_nums_of_1(num)))
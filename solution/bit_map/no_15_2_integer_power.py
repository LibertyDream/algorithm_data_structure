'''面试题15-2：2的整数次幂判断

用一条语句判断一个整数是不是2的整数次方
-------------
Example
input: 4
output: True
--------------
一个整数如果是2的整数次方，那么它的二进制表示中有且只有一位是1，而其他所有位都是0
'''

def is_integer_power(value):
    if not isinstance(value, int):
        return False

    return True if value & (value - 1) == 0 else False

if __name__ == "__main__":
    print('num, is_integer_power_of_2')
    for i in range(10):
        print('%d, %s' % (i, is_integer_power(i)))

    print((1<<63) - 1)
    print(2**63 -1)
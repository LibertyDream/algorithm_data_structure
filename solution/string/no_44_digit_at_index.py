'''面试题44：数字序列中某一位的数字

数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
'''

def digit_of_index(idx):

    if idx < 0:
        return -1
    
    digit = 1

    # 跨数位找基线
    while __digit_nums(digit)*digit < idx:
        idx -= __digit_nums(digit) * digit
        digit += 1

    # 确认几位数后找偏移
    target = pow(10, digit - 1) + idx // digit

    # 确认是哪个数后，余数是几就是左数第几位
    bias = digit - idx % digit
    for _ in range(bias):
        target //= 10
    
    return target % 10

def __digit_nums(digit):

    count = pow(10, digit - 1)
    return 9 * count

if __name__ == "__main__":

    # 12345678910111213......
    print(digit_of_index(11))
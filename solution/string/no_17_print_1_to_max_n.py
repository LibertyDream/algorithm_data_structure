'''面试题17：打印从1到最大的n位数

输入数字n，按顺序打印出从1到最大的n位十进制数。
---------------
Example
input:3
output:1,2,3,...,999
---------------
如果面试题是关于n位的整数并且没有限定n的取值范围，或者输入任意大小的整数，
那么这道题目很有可能是需要考虑大数问题的。字符串、数组可以用来表示大数。
'''

def print_1_to_max_of_n(n):

    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be positive integer')
    
    numbers = [0] * n

    __recur_print(numbers, n, 0)

def __recur_print(numbers, length, index):
    if index == length:
        __print_numbers(numbers)
        return

    for i in range(10):
        numbers[index] = i
        __recur_print(numbers, length, index + 1)

def __print_numbers(numbers):        

    is_begin = True
    for i in range(len(numbers)):
        if is_begin and numbers[i] != 0:
            is_begin = False
        if not is_begin:
            print(numbers[i], end='')
    print(end='\t')


if __name__ == '__main__':
    
    print_1_to_max_of_n(2)
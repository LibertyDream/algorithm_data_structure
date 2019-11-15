'''面试题43：1~n整数中1出现的次数

输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。
--------------
Example:
input:12
output: 5  # 1,10,11,12
'''

def nums_of_1(n):
    if n < 0:
        return 0
    
    return __nums_of_1(str(n), 0)

def __nums_of_1(n_str, idx):

    if n_str is None or idx == len(n_str) or n_str[idx] < '0' or n_str[idx] > '9':
        return 0

    first = int(n_str[idx])

    # 个位判断
    if idx == len(n_str)-1 and first > 0:
        return 1
    
    if idx == len(n_str)-1 and first == 0:
        return 0

    # 首位判断
    if first > 1:
        digit_1 = pow(10,len(n_str) - 1 - idx)
    if first == 1:
        digit_1 = int(n_str[idx+1:])+ 1
    
    # 确认首位后，其他位置的排列组合数
    digit_2 = first * (len(n_str) - 1 - idx) * pow(10,len(n_str) - 2 - idx)

    # len(n_str) - idx 位数中 1 出现的次数
    digit_3 = __nums_of_1(n_str, idx + 1)

    return digit_1 + digit_2 + digit_3    

if __name__ == '__main__':

    print(nums_of_1(12))
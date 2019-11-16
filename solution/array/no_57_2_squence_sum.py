'''面试题57-2:和为s的连续正数序列

输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
--------------
Example:
input:15
output: 1,2,3,4,5 4,5,6 7,8
'''

def squence_sum(target):

    if target < 3:
        return None

    small = 1
    big = 2
    cur_sum = small + big
    mid = (target + 1) >> 1
    ret = []

    while small < mid:
        if cur_sum == target:
            ret.append([x for x in range(small,big+1)])

        while cur_sum > target and small < mid:
            cur_sum -= small
            small += 1
            if cur_sum == target:
                 ret.append([x for x in range(small,big+1)])

        big += 1
        cur_sum += big

    return ret

if __name__ == '__main__':
    
    targets = [9, 15, -2, 4]
    for target in targets:
        print(squence_sum(target))
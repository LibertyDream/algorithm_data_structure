'''面试题49：丑数

我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到大的顺序的第1500个丑数。
例如，6、8都是丑数，但14不是，因为它包含因子7。习惯上我们把1当作第一个丑数。
-------------
遍历思路--提示、互动--改进实现
'''

def find_ugly_num(index):

    if index <= 0:
        return -1

    ugly_nums = [0] * index

    ugly_nums[0] = 1

    idx_2_base = idx_3_base = idx_5_base = 0
    for idx in range(1, index):
        min_num = __min(ugly_nums[idx_2_base] * 2, 
                        ugly_nums[idx_3_base] * 3, 
                        ugly_nums[idx_5_base] * 5)
        ugly_nums[idx] = min_num

        while ugly_nums[idx_2_base] * 2 <= ugly_nums[idx]:
            idx_2_base += 1
        while ugly_nums[idx_3_base] * 3 <= ugly_nums[idx]:
            idx_3_base += 1
        while ugly_nums[idx_5_base] * 5 <= ugly_nums[idx]:
            idx_5_base += 1

        idx += 1

    return ugly_nums[index - 1]

def __min(a,b,c):

    temp = a if a < b else b
    return temp if temp < c else c
        
if __name__ == "__main__":

    indexes = [-1, 2, 3, 1500]
    for idx in indexes:
        print(find_ugly_num(idx))


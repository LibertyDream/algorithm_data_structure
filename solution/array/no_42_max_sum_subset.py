'''面试题42：连续子数组的最大和

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为O（n）。
----------------
Example:
input:[1,-2,3,10,-4,7,2,-5]
output:18  # [3,10,-4,7,2]
'''
import sys

def max_sum_of_subarrays(arr):

    if arr is None or len(arr) == 0:
        return False, 0

    ret = cur_sums = -sys.maxsize
    for x in arr:
        if cur_sums <= 0:
            cur_sums = x
        else:
            cur_sums += x

        if cur_sums > ret:
            ret = cur_sums
    
    return True, ret

if __name__ == "__main__":

    datas = [[1,-2,3,10,-4,7,2,-5],[1,2,3,4,5],[-1,-2,-3,-4,-5],None,[]]
    
    for data in datas:
        valid, res = max_sum_of_subarrays(data)
        if valid:
            print(res)
        else:
            print('Invalid data')
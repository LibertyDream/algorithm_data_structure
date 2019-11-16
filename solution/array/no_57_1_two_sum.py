'''面试题57-1：和为s的两个数字

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。
------------
Example:
input:[1,2,4,7,11,15]
output:(4,11)
'''

def two_sum(array, target):

    if array is None or len(array) == 0:
        return None

    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] < target:
            left += 1
        elif array[left] + array[right] > target:
            right -= 1
        else:
            return array[left], array[right]
    
    return None

if __name__ == "__main__":

    datas = [[[1,2,4,7,11,15],15],[[1,2,4,6],20],[None, 1]]

    for data in datas:
        nums, target = data
        print(two_sum(nums, target))

'''面试题11：旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
----------------
Example
input:[3，4，5，1，2]
output:1
---------------
一旦有顺序性，最大最小值和二分查找多半会有用武之地
'''

def min_val(arr):

    if arr is None or len(arr) == 0:
        return None
    
    ret = pre = 0
    post = len(arr) - 1
    while arr[post] <= arr[pre]:

        if post == pre + 1:

            ret = post
            break
        
        mid = pre + (post - pre) // 2
        if arr[mid] == arr[post] == arr[pre]:
            return  __min_val_iter(arr)
        if arr[mid] >= arr[pre]:
            pre = mid
        else: # arr[mid] < arr[pre]
            post = mid
    
    return arr[ret]

def __min_val_iter(arr):

    ret_idx = 0
    for x in arr:
        if x < arr[ret_idx]:
            ret_idx = x
    return arr[ret_idx]

if __name__ == "__main__":

    array1 = [3,4,5,1,2]
    array2 = [1,0,1,1,1]
    array3 = [1,2,3,4,5]

    print(min_val([]))
    print(min_val(None))
    print(min_val(array1))
    print(min_val(array2))
    print(min_val(array3))
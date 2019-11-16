'''面试题53-3:数组中数值和下标相等的元素

假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，
找出数组中任意一个数值等于其下标的元素。
-----------------
Example:
input:[-3，-1，1，3，5]
output:3
'''

def same_as_index(array):

    if array is None or len(array) == 0:
        return -1

    start = 0
    end = len(array) - 1
    while start <= end:
        
        mid = start + ((end - start) >> 1)

        if array[mid] == mid:
            return mid
        if array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

if __name__ == "__main__":

    datas = [[],None,[1],[0],[-3,-2,-1,3,5],[-1,1],[1,2,3]]
    for data in datas:
        print(data, same_as_index(data))
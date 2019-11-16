'''面试题53-1：在排序数组中查找数字

统计一个数字在排序数组中出现的次数。
--------------
Example:
input:[1，2，3，3，3，3，4，5] 3
output:4
'''

def statistic_nums(sorted_arr, number):

    if sorted_arr is None or len(sorted_arr) == 0:
        return -1

    start = __get_start_idx(sorted_arr, number, 0, len(sorted_arr)-1)
    end = __get_end_idx(sorted_arr, number, 0, len(sorted_arr)-1)

    if start > -1 and end > -1:
        return end - start + 1
    return -1
    
def __get_start_idx(arr, num, start, end):

    if start > end:
        return -1

    mid = start + ((end - start) >> 1)
    
    if arr[mid] < num:
        start = mid + 1
    elif arr[mid] > num:
        end = mid - 1
    else:
        if (mid > 0 and arr[mid-1] != num) or mid == 0:
            return mid
        else:
            end = mid - 1
    
    return __get_start_idx(arr, num, start, end)


def __get_end_idx(arr, num, start, end):

    if start > end:
        return -1

    mid = start + ((end - start) >> 1)
    
    if arr[mid] < num:
        start = mid + 1
    elif arr[mid] > num:
        end = mid - 1
    else:
        if (mid < len(arr) - 1 and arr[mid+1] != num) or mid == len(arr) - 1:
            return mid
        else:
            start = mid + 1
    
    return __get_end_idx(arr, num, start, end)

if __name__ == "__main__":

    datas = [[[1,2,3,3,3,3,4,5], 3],[[1,2,2,4,5],3],[[1,2,3,4],1],[None,2]]
    for data in datas:
        arr, num = data
        print(statistic_nums(arr, num))
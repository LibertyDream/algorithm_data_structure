import sort_helper as sh
import insertion_sort as ins

def merge_sort(*arr):

    arr = list(arr)

    __merge_sort(arr, 0, len(arr)-1)

    return arr
    
def __merge_sort(arr, left: int, right: int):
    '''
    对 arr 中 [left, right] 范围内的元素进行归并排序
    '''
    if right - left <= 15:

        for i in range(left + 1, right + 1):
            temp = arr[i]
            j = i
            while j > left and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
        
        return

    mid = left + (right - left) // 2
    __merge_sort(arr, left, mid)
    __merge_sort(arr, mid + 1, right)

    if arr[mid] > arr[mid + 1]:
        __merge(arr, left, mid, right)

def __merge(arr, left: int, mid: int, right: int):
    temp = [None] * (right - left + 1)
    for i in range(left, right + 1):
        temp[i - left] = arr[i]

    l_idx = left
    r_idx = mid + 1
    
    for insert_idx in range(left, right + 1):

        if l_idx > mid:
            arr[insert_idx] = temp[r_idx - left]
            r_idx += 1
        elif r_idx > right:
            arr[insert_idx] = temp[l_idx - left]
            l_idx += 1
        elif temp[l_idx - left] < temp[r_idx - left]:
            arr[insert_idx] = temp[l_idx - left]
            l_idx += 1
        else:
            arr[insert_idx] = temp[r_idx - left]
            r_idx += 1

def merge_sort_bottom_up(*arr):
    '''
        非递归实现，步长取值从 1 至 n (元素个数)，2 倍增长率

        非递归实现没有用到数组随机访问的特性，所以适用于对链表一类数据结构快速排序
    '''
    arr = list(arr)

    gap = 1
    while gap < len(arr):
        i = 0
        while i + gap < len(arr):
            __merge(arr, i, i + gap -1, min(i + gap + gap -1, len(arr)-1))
            i += 2 * gap
        gap *= 2

    return arr

if __name__ == "__main__":
    
    nums = 10000
    input_arr = sh.generate_int_array(nums, 0, nums)
    copy_arr1 = copy_arr2 = input_arr.copy()

    # sh.sort_cost('insertion_sort', ins.insertion_sort, copy_arr1)
    sh.sort_cost('merge_sort', merge_sort, input_arr)
    sh.sort_cost('merge_sort_bottom_up', merge_sort_bottom_up,copy_arr2)
    input_arr = sh.generate_nearly_ordered_array(nums,10)
    copy_arr1 = input_arr.copy()
    copy_arr2 = input_arr.copy()

    sh.sort_cost('insertion_sort', ins.insertion_sort, copy_arr1)
    sh.sort_cost('merge_sort', merge_sort, input_arr)
    sh.sort_cost('merge_sort_bottom_up', merge_sort_bottom_up, copy_arr2)



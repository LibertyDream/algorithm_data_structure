import sort_helper as sh
import merge_sort as ms
import random

def quick_sort(*arr):

    arr = list(arr)

    __quick_sort(arr, 0, len(arr) - 1)

    return arr

def __quick_sort(arr, left, right):

    if right - left <= 15:

        for i in range(left + 1, right + 1):
            j = i
            temp = arr[i]
            while j > left and arr[j - 1] >temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp

        return

    pos = __partition(arr, left, right)
    __quick_sort(arr, left, pos - 1)
    __quick_sort(arr, pos + 1, right)

def __partition(arr, left, right):
    '''
        分割数组返回分割点
    '''
    swap_idx = random.randint(left, right)
    arr[swap_idx], arr[left] = arr[left], arr[swap_idx]
    val = arr[left]

    # [left + 1, lt) <= val,(gt, right] >= val
    gt = right
    lt = left + 1

    while True:
        while lt <= right and arr[lt] < val: 
            lt += 1
        while gt >= left and arr[gt] > val:  
            gt -= 1
        if lt > gt: break
        
        arr[lt],arr[gt] = arr[gt], arr[lt]

        lt += 1
        gt -= 1
    
    arr[left], arr[gt] = arr[gt], arr[left]

    return gt

if __name__ == "__main__":

    nums = 100000

    print('Random samples test: size=%d' % nums)
    arr = sh.generate_int_array(nums, 0, nums)
    copy_arr = arr.copy()
    sh.sort_cost('quick_sort', quick_sort,arr)
    sh.sort_cost('merge_sort', ms.merge_sort,copy_arr)

    swap = 100
    print('Nearly ordered samples test: size=%d swap=%d' % (nums,swap))
    arr = sh.generate_nearly_ordered_array(nums,100)
    copy_arr = arr.copy()
    sh.sort_cost('quick_sort', quick_sort,copy_arr)
    sh.sort_cost('merge_sort', ms.merge_sort,arr)

    print('Duplicate samples test: size=%d' % nums)
    arr = sh.generate_int_array(nums, 0, 10)
    copy_arr = arr.copy()
    sh.sort_cost('quick_sort', quick_sort,copy_arr)
    sh.sort_cost('merge_sort', ms.merge_sort,arr)

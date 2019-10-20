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
    __quick_sort(arr, left, pos)
    __quick_sort(arr, pos + 1, right)

def __partition(arr, left, right):
    '''
        分割数组返回分割点 pos，满足 [left, pos-1] < pos,[gt, i) > pos, i 为当前考察点
    '''
    swap_idx = random.randint(left, right)
    arr[swap_idx], arr[left] = arr[left], arr[swap_idx]
    val = arr[left]

    gt = left + 1

    for i in range(left + 1, right + 1):
        if arr[i] < val:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt += 1
    
    arr[left], arr[gt-1] = arr[gt-1], arr[left]

    return gt - 1

if __name__ == "__main__":

    nums = 100000

    arr = sh.generate_int_array(nums, 0, nums)
    copy_arr = arr.copy()
    sh.sort_cost('quick_sort', quick_sort,arr)
    sh.sort_cost('merge_sort', ms.merge_sort,copy_arr)

    arr = sh.generate_nearly_ordered_array(nums,100)
    copy_arr = arr.copy()
    sh.sort_cost('quick_sort', quick_sort,copy_arr)
    sh.sort_cost('merge_sort', ms.merge_sort,arr)
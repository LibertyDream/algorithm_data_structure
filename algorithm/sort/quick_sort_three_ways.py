import sort_helper as sh
import quick_sort as qs
import merge_sort as ms
import random

def quick_sort_three_ways(*arr):

    arr = list(arr)

    __quick_sort_three_ways(arr, 0, len(arr) - 1)

    return arr

def __quick_sort_three_ways(arr, left, right):

    if right - left <= 15:

        for i in range(left + 1, right + 1):
            temp = arr[i]
            j = i
            while j > left and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
        return

    lt, gt = __partition(arr, left, right)
    __quick_sort_three_ways(arr, left, lt)
    __quick_sort_three_ways(arr, gt, right)

def __partition(arr, left, right):

    swap_idx = random.randint(left, right)
    arr[swap_idx], arr[left] = arr[left], arr[swap_idx]
    val = arr[left]

    # [left + 1, lt] < v
    lt = left
    # [lt + 1, i) == v
    i = left + 1
    # [gt, right] > v
    gt = right + 1

    while i < gt:

        if arr[i] < val:
            lt += 1
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
        elif arr[i] > val:
            gt -= 1
            arr[i], arr[gt] = arr[gt], arr[i]            
        else:
            i += 1
    
    arr[left], arr[lt] = arr[lt], arr[left]

    return lt - 1, gt


if __name__ == "__main__":
    nums = 100000

    print('Random samples test: size=%d' % nums)
    arr = sh.generate_int_array(nums, 0, nums)
    copy_arr2 = copy_arr = arr.copy()
    sh.sort_cost('quick_sort', qs.quick_sort,arr)
    sh.sort_cost('merge_sort', ms.merge_sort,copy_arr)
    sh.sort_cost('quick_sort_three_ways', quick_sort_three_ways, copy_arr2)

    swap = 100
    print('Nearly ordered samples test: size=%d swap=%d' % (nums,swap))
    arr = sh.generate_nearly_ordered_array(nums,100)
    copy_arr2 = copy_arr = arr.copy()
    sh.sort_cost('quick_sort', qs.quick_sort,copy_arr)
    sh.sort_cost('merge_sort', ms.merge_sort,arr)
    sh.sort_cost('quick_sort_three_ways', quick_sort_three_ways, copy_arr2)

    print('Duplicate samples test: size=%d' % nums)
    arr = sh.generate_int_array(nums, 0, 10)
    copy_arr2 = copy_arr = arr.copy()
    sh.sort_cost('quick_sort', qs.quick_sort,copy_arr)
    sh.sort_cost('merge_sort', ms.merge_sort,arr)
    sh.sort_cost('quick_sort_three_ways', quick_sort_three_ways, copy_arr2)
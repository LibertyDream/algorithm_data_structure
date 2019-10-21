import sort_helper as sh
import merge_sort as ms
import quick_sort_three_ways as qst
from max_heap import MaxHeap

def heap_sort(*arr):
    arr = list(arr)

    heap = MaxHeap(arr)
    arr= []
    for i in range(len(arr)-1, -1, -1):
        arr[i] = heap.remove()

    return arr

def in_place_heap_sort(*arr):

    arr = list(arr)
    length = len(arr)
    for i in range((length-2)//2, -1, -1):
        __shift_down(arr, length, i)
    
    for i in range(length):
        arr[0], arr[length - i - 1] = arr[length - i - 1], arr[0]
        __shift_down(arr, length-i-1, 0)

    return arr

def __shift_down(arr, size, index):

    while 2*index + 1 < size:
        swap = 2*index + 1
        if swap + 1 < size and arr[swap + 1] > arr[swap]:
            swap += 1
        
        if arr[swap] < arr[index]:
            break

        arr[swap], arr[index] = arr[index], arr[swap]

        index = swap

if __name__ == "__main__":
    
    nums = 100000

    print('Random samples test: size=%d' % nums)
    arr = sh.generate_int_array(nums, 0, nums)
    copy_arr3 = copy_arr2 = copy_arr = arr.copy()
    sh.sort_cost('heap_sort', heap_sort, arr)
    sh.sort_cost('in_place_heap_sort', in_place_heap_sort, copy_arr3)
    sh.sort_cost('merge_sort', ms.merge_sort,copy_arr)
    sh.sort_cost('quick_sort_three_ways', qst.quick_sort_three_ways, copy_arr2)

    swap = 100
    print('\nNearly ordered samples test: size=%d swap=%d' % (nums,swap))
    arr = sh.generate_nearly_ordered_array(nums,100)
    copy_arr3 = copy_arr2 = copy_arr = arr.copy()
    sh.sort_cost('heap_sort', heap_sort, arr)
    sh.sort_cost('in_place_heap_sort', in_place_heap_sort, copy_arr3)
    sh.sort_cost('merge_sort', ms.merge_sort,copy_arr)
    sh.sort_cost('quick_sort_three_ways', qst.quick_sort_three_ways, copy_arr2)

    print('\nDuplicate samples test: size=%d' % nums)
    arr = sh.generate_int_array(nums, 0, 10)
    copy_arr3 = copy_arr2 = copy_arr = arr.copy()
    sh.sort_cost('heap_sort', heap_sort, arr)
    sh.sort_cost('in_place_heap_sort', in_place_heap_sort, copy_arr3)
    sh.sort_cost('merge_sort', ms.merge_sort,copy_arr)
    sh.sort_cost('quick_sort_three_ways', qst.quick_sort_three_ways, copy_arr2)
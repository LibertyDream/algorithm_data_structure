'''面试题40：最小的k个数

输入n个整数，找出其中最小的k个数。
---------------
Example:
input:[4、5、1、6、2、7、3、8] 4
output:1、2、3、4
---------------
如果面试时遇到的面试题有多种解法，并且每种解法都各有优缺点，
那么我们要向面试官问清楚题目的要求、输入的特点，从而选择最合适的解法。
'''
import random
import heapq as hq

def __partition(arr, left, right):

    if left >= right:
        return left
    
    idx = random.randint(left, right)
    arr[left], arr[idx] = arr[idx], arr[left]

    lt = left
    gt = right + 1
    idx = left
    while idx < gt:

        if arr[idx] < arr[left]:
            lt += 1
            arr[idx], arr[lt] = arr[lt], arr[idx]
            idx += 1
        elif arr[idx] > arr[left]:
            gt -= 1
            arr[idx], arr[gt] = arr[gt], arr[idx]
        else:
            idx += 1
    
    arr[left], arr[lt] = arr[lt], arr[left]
    return lt


def least_nums_partition(nums, k):
    ''' O(n)，会修改数组，不适合海量数据'''
    if nums is None or k <= 0:
        return None
    if len(nums) <= k:
        return nums

    begin = 0
    end = len(nums) - 1

    idx = __partition(nums, begin, end)
    while idx != k - 1:
        if idx > k - 1:
            end = idx - 1
            idx = __partition(nums, begin, end)
        elif idx < k - 1:
            begin = idx + 1
            idx = __partition(nums, begin, end)
    
    return [nums[x] for x in range(k)]

def least_nums_heap(nums, k):
    ''' O(nlogk),不改变数组，适合海量数据'''

    if nums is None or k <= 0:
        return None
    
    if len(nums) <= k:
        return nums

    heap = []
    count = 0
    for x in nums:
        if count < k:
            hq.heappush(heap,-x)
            count += 1
        else:
            cur = -hq.heappop(heap)
            if cur > x:
                cur = -x
            hq.heappush(heap,cur)

    return heap

if __name__ == "__main__":

    datas = [[4,5,1,6,2,7,3,8],[5,3,2,6,2,3,7,4],[],None,[1]]
    k = 4
    for data in datas:
        print(least_nums_partition(data,k))
        print(least_nums_heap(data,k))
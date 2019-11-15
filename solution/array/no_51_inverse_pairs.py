'''面试题51：数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
----------------
Example:
input:[7，5，6，4]
output:5  #(7，6)、（7，5）、（7，4）、（6，4）和（5，4）
'''

def inverse_pairs(arr):

    if arr is None or len(arr) == 0:
        return -1

    return __inverse_pairs(arr, 0, len(arr)-1)

def __inverse_pairs(arr, start, end):

    if start == end:
        return 0
    
    mid = start + (end - start) // 2
    left = __inverse_pairs(arr,start,mid)
    right = __inverse_pairs(arr,mid+1,end)

    copy = [0] * (end - start + 1)
    count = 0
    l_idx = start
    r_idx = mid+1
    idx = 0
    while l_idx <= mid and r_idx <= end:

        if arr[l_idx] > arr[r_idx]:
            count += mid - l_idx + 1
            copy[idx] = arr[r_idx]
            r_idx += 1
        else:
            copy[idx] = arr[l_idx]
            l_idx+=1
        
        idx += 1
    while l_idx <= mid:
        copy[idx] = arr[l_idx]
        l_idx += 1
        idx += 1
    while r_idx <= end:
        copy[idx] = arr[r_idx]
        r_idx += 1
        idx += 1
    
    for i in range(len(copy)):
        arr[start + i] = copy[i]
    
    return count + left + right

if __name__ == "__main__":

    datas = [None, [], [3,2,1], [1,2,3], [7,5,6,4]]
    for data in datas:
        print(inverse_pairs(data))
import random as rd
import string
import time

def generate_int_array(nums, rangel, ranger):
    if ranger < rangel:
        raise ValueError("ranger must be greater than rangel")

    res = []
    for i in range(nums):
        res.append(rd.randint(rangel,ranger))
    
    return res

def generate_float_array(nums, rangel, ranger):
    if ranger < rangel:
        raise ValueError("ranger must be greater than rangel")

    res = []
    for i in range(nums):
        res.append(rd.uniform(rangel,ranger))
    
    return res

def generate_string_array(nums,length):

    return [''.join(rd.sample(string.ascii_letters + string.digits,length)) for i in range(nums)]

def print_array(arr):

    for i in arr:
        print(i, end=" ")
    print()

def sort_cost(func_name, function, arr):

    start = time.time()

    res = function(*arr)

    end = time.time()

    is_sorted(res)

    print("%s cost: %fs" % (func_name, end - start))
    
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            raise ValueError("Array is not sorted")

def generate_nearly_ordered_array(nums, swap_times):

    res = []
    for i in range(nums):
        res.append(i)
    
    for i in range(swap_times):
        _x = rd.randint(0,nums)
        _y = rd.randint(0,nums)
        res[_x], res[_y] = res[_y], res[_x]
    
    return res


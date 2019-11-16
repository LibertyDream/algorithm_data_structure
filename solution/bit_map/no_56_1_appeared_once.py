'''面试题56-1:数组中只出现一次的两个数字

一个整型数组里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
要求时间复杂度是O（n），空间复杂度是O（1）
------------
Example:
input:[2,4,3,6,3,5,5,2]
output:4,6
-----------
一个数和自己异或得 0，出现两次的凭此可以抵消
'''

def appeared_once(array):
    if array is None or len(array) < 2:
        return None

    lt_1, lt_2 = __get_appeared_once_arr(array)
    ret_1 = __find_appeared_once(lt_1)
    ret_2 = __find_appeared_once(lt_2)

    if ret_1 is None or ret_2 is None:
        return None
    return ret_1, ret_2

def __get_appeared_once_arr(array):

    mix_out = 0
    
    for x in array:
        mix_out ^= x

    div_idx = 0
    while (mix_out & 1 == 0) and (mix_out != 0):
        mix_out = mix_out >> 1
        div_idx += 1

    lt_1 = []
    lt_2 = []

    for x in array:
        if __div_idx_is_1(x, div_idx):
            lt_1.append(x)
        else:
            lt_2.append(x)
    return lt_1, lt_2

def __div_idx_is_1(num, div_idx):

    num = num >> div_idx
    
    return num & 1

def __find_appeared_once(array):
    if array is None or len(array) == 0:
        return None

    ret = 0

    for x in array:
        ret ^= x

    return ret if ret!= 0 else None

if __name__ == "__main__":

    datas = [[2,4,3,6,3,5,5,2],[1,2],[],None,[2,2,3,3]]
    for data in datas:
        print(appeared_once(data))
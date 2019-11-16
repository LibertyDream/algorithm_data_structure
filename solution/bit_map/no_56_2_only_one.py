'''面试题56-2: 数组中唯一只出现一次的数字

在一个数组中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
-------------
Example:
input:[2,2,2,1,3,3,3]
output:1
'''

def appeared_once(array):
    if array is None or len(array) < 1:
        return -1

    bits = [0] * 32
    for num in array:
        bin_str = str(bin(num))[2:]
        for i in range(len(bin_str)-1, -1, -1):
            if bin_str[i] == '1':
                bits[31-i] += 1
    ret = 0
    for i in range(len(bits)):
        ret = ret << 1
        ret += bits[i] % 3

    return ret if ret != 0 else -1


if __name__ == "__main__":

    datas = [[2,2,2,4,4,4],None,[1],[2,3,2,4,2,4,4]]
    for data in datas:
        print(appeared_once(data))
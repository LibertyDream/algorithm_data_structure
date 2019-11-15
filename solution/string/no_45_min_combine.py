'''面试题45：把数组排成最小的数

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
----------------
Example:
input:[3,32,321]
output:321323
----------------
排序规则设计，规则证明（自反，对称，传递），算法证明，大数防治
'''

class NewString(object):

    def __init__(self, string):
        self.string = str(string)
    
    def __lt__(self, other):
        return self.string + other.string < other.string + self.string
    
    def __eq__(self, other):

        return self.string + other.string == other.string + self.string

    def __str__(self):
        return self.string

def min_combine(nums):

    if nums is None or len(nums)== 0:
        return None
    
    for num in nums:
        if num <= 0:
            raise ValueError('element must be positive integer')

    str_nums = [NewString(i) for i in nums]

    str_nums.sort()

    ret = ''
    for i in str_nums:
        ret += str(i)
    
    return ret

if __name__ == '__main__':
    
    datas = [[3,32,321],[1],[],None,[2,12,-1]]

    for data in datas:
        print(min_combine(data))

    

'''面试题50-1：字符串中第一个只出现一次的字符

Example:
input: abaccdeff
output: b
------------------
如果需要判断多个字符是不是在某个字符串里出现过或者统计多个字符在某个字符串中出现的次数，
那么我们可以考虑基于数组创建一个简单的哈希表，这样可以用很小的空间消耗换来时间效率的提升。
'''

def find_first_appeared_once(string):

    if string is None or len(string) == 0:
        return None

    appear_times = [0] * 256
    for idx in range(len(string)):
        appear_times[ord(string[idx])] += 1
    
    for idx in range(len(string)):
        if appear_times[ord(string[idx])] == 1:
            return string[idx]
    
    return None

if __name__ == '__main__':

    datas = ['abaccdeff','a', 'aabb', '', None]

    for data in datas:
        print(find_first_appeared_once(data))
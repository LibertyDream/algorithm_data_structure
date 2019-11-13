'''面试题38：字符串的排列

输入一个字符串，打印出该字符串中字符的所有排列。
------------
Example:
input:abc
output:abc,acb,bac,bca,cab,cba
------------------
如果面试题是按照一定要求摆放若干个数字，则可以先求出这些数字的所有排列，
然后一一判断每个排列是不是满足题目给定的要求。
'''

def permutation(string):
    if string is None or string=='':
        return string
    
    ls_string = [x for x in string]

    __permutation(ls_string, 0)

def __permutation(string, begin):

    if begin == len(string):
        print(''.join(string), end=' ')
    else:
        for idx in range(begin, len(string)):
            string[idx], string[begin] = string[begin], string[idx]
            __permutation(string, begin + 1)
            string[idx], string[begin] = string[begin], string[idx]

if __name__ == "__main__":

    string = 'abc'
    permutation(string)
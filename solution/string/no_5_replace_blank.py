'''面试题5：替换空格

请实现一个函数，把字符串中的每个空格替换成“%20”
-----------
Example
input: 'We are happy'
output: 'We%20are%20happy'
---------------
合并数组的时候，如果从前向后涉及大量交换操作，不妨试试从后向前提高效率
'''

def repalce_blank(string, length): # length 为 string 最大长度
    
    if string is None:
        return
    
    blank_num = 0
    for x in string:
        if x == ' ':
            blank_num += 1
    
    new_length = len(string) + 2 * blank_num

    if new_length > length:
        return

    char = [None] * new_length
    i = len(string) - 1
    j = new_length - 1
    while i >= 0:

        if string[i] == ' ':
            char[j] = '0'
            j -= 1
            char[j] = '2'
            j -= 1
            char[j] = '%'
            j -= 1
            i -= 1
        else:
            char[j] = string[i]
            j -= 1
            i -= 1

    return ''.join(char)

if __name__ == "__main__":
    
    string1 = 'We are happy'
    string2 = ' '
    string3 = '  I am  happy '
    
    print(repalce_blank(None,20))
    print(repalce_blank('',20))
    print(repalce_blank(string1,15))
   
    print(repalce_blank(string1,20))
    print(repalce_blank(string2,20))
    print(repalce_blank(string3,40))
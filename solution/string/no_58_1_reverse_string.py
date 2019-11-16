'''面试题58-1：翻转单词顺序

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。
------------
Example:
input:I am a student.
output:student. a am I
'''

def reverse_word_seq(string):

    if string is None or len(string) == 0:
        return string

    temp = string.split(' ')
    start = 0
    end = len(temp) - 1
    while start < end:
        temp[start], temp[end] = temp[end], temp[start]
        start += 1
        end -= 1
    return ' '.join(temp)

if __name__ == '__main__':

    strings =['I am a student.','yes','',None]
    for string in strings:
        print(string, reverse_word_seq(string))
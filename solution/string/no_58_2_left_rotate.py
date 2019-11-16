'''面试题58-2:左旋转字符串

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
---------------
input: abcdefg 2
output: cdefgab
'''

def left_rotate(string, n):

    if string is None or len(string) == 0:
        return None

    if n < 0 or n >len(string):
        return None

    str_arr = [x for x in string]

    begin = 0
    div = n - 1
    end = len(string) - 1
    __reverse(str_arr, begin, div)
    __reverse(str_arr, div+1, end)
    __reverse(str_arr, begin, end)

    return ''.join(str_arr)

def __reverse(str_arr, begin, end):

    while begin < end:
        str_arr[begin], str_arr[end] = str_arr[end], str_arr[begin]
        begin += 1
        end -= 1


if __name__ == "__main__":

    string = 'abcdefg'
    rotate = 2
    print('"%s" left rotate %d: %s' % (string, rotate, left_rotate(string, rotate)))
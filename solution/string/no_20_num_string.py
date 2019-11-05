'''面试题20：表示数值的字符串

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）
----------------
Example
input:"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"
output:True,True,True,True,True
input:"12e"、"1a3.14"、"1.2.3"、"+-5"、"12e+5.4"
output:False,False,False,False,False
-------------------
python 字符可以直接比较，ord()可以获取unicode值
'''

def is_numeric(string):

    if string is None or len(string) < 1:
        return False

    numeric, idx = __int_judge(string,0)

    if  idx < len(string) and string[idx] == '.':
        temp_judge, idx = __unsigned_int_judge(string,idx+1)
        numeric = temp_judge or numeric
    
    if idx < len(string) and (string[idx] == 'e' or string[idx] == 'E'):
        temp_judge, idx = __int_judge(string,idx+1)
        numeric = temp_judge and numeric

    return idx == len(string) and numeric


def __int_judge(string, idx):
    if idx < len(string) and (string[idx] == '+' or string[idx] == '-'):
        idx += 1
    return __unsigned_int_judge(string,idx)

def __unsigned_int_judge(string, idx):
    before = idx
    while idx < len(string) and string[idx] >= '0' and string[idx] <= '9':
        idx += 1

    return idx > before, idx

if __name__ == '__main__':

    datas = ["+100","5e2","-123","3.1416","-1E-16",
            "12e","1a3.14","1.2.3","+-5","12e+5.4"]

    for data in datas:
        print('%s:%s'%(data, is_numeric(data)))
'''面试题46：把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成“a”，1翻译成“b”，…，
11翻译成“1”，…，25翻译成“z”。一个数字可能有多个翻译。请编程实现一个函数，
用来计算一个数字有多少种不同的翻译方法。
--------------
Example:
input:12258
output:5  #“bccfi”、“bwfi”、“bczi”、“mcfi”和“mzi”
----------------
递归分析，循环实现，避免重复计算
'''

def num_trans_count(num):

    if num is None or num < 0:
        return None
    
    str_num = str(num)

    idx = len(str_num) - 1
    counts = [0] * len(str_num)
    while idx >= 0:
        count = 0
        if idx < len(str_num) - 1:
           count = counts[idx+1]
        else:
            count = 1

        if idx < len(str_num) - 1:
            char = int(str_num[idx:idx+2])
            if char > 9 and char < 26:
                if idx < len(str_num) - 2:
                    count += counts[idx+2]
                else:
                    count += 1
        
        counts[idx] = count
        idx -= 1

    return counts[0]

if __name__ == "__main__":

    datas = [12258,3,None,-1]
    for data in datas:
        print(num_trans_count(data))
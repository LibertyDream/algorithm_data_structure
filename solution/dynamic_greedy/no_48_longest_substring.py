'''面试题48：最长不含重复字符的子字符串

请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
假设字符串中只包含a~z的字符。
---------------
Example:
input:arabcacfr
output:4  # acfr
'''

def longest_substring_without_duplication(string):

    if string is None or len(string) == 0:
        return -1
    
    occured = [-1] * 26
    cur_len = 0
    max_len = 0
    for i in range(len(string)):
        prev = occured[ord(string[i])-ord('a')]
        if prev < 0 or i - prev > cur_len:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            
            cur_len = i - prev
        
        occured[ord(string[i]) - ord('a')] = i

    if cur_len > max_len:
        max_len = cur_len

    return max_len

if __name__ == '__main__':

    datas = ['arabcacfr','a',None,'']
    for data in datas:
        print(longest_substring_without_duplication(data))
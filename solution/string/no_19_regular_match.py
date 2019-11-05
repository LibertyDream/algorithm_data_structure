'''面试题19：正则表达式匹配

请实现一个函数用来匹配包含，和*的正则表达式。模式中的字符表示任意一个字符，
而*表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
-------------------
Example
input:"aaa","a.a"
output:True

input:"aaa","ab*ac*a"
output:True

input:"aaa","aa.a"
output:False

input:"aaa","ab*a"
output:False
'''

def re_match(string, pattern):
    if string is None or pattern is None:
        raise ValueError('string or pattern is None')

    return __match(string, pattern, 0, 0)

def __match(string, pattern, str_idx, pat_idx):

    if str_idx == len(string) and pat_idx >= len(pattern):
        return True
    if str_idx < len(string) and pat_idx >= len(pattern):
        return False
    
    if pat_idx+1 < len(pattern) and pattern[pat_idx + 1] == '*':
        if string[str_idx] == pattern[pat_idx] or (str_idx < len(string) and pattern[pat_idx] == '.'):
            return (__match(string, pattern, str_idx + 1, pat_idx + 2) 
            or __match(string, pattern, str_idx + 1, pat_idx)
            or __match(string, pattern, str_idx, pat_idx + 2))

        return __match(string, pattern, str_idx, pat_idx + 2)

    if str_idx == len(string):
        return True if pattern[pat_idx] == '*' else False
    else:
        if string[str_idx] == pattern[pat_idx] or (str_idx < len(string) and pattern[pat_idx] == '.'):
            return __match(string, pattern, str_idx + 1, pat_idx + 1)
        
        return False


if __name__ == "__main__":

    string = 'aaa'

    patterns = ['a.a','ab*ac*a','aa.a','ab*a','.*']

    for pattern in patterns:
        print('%s, %s, %s' %(string, pattern, re_match(string, pattern)))
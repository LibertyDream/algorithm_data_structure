'''面试题50-2：字符流中第一个只出现一次的字符。

请实现一个函数，用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"g0”时，第一个只出现一次的字符是g；
当从该字符流中读出前6个字符"google”时，第一个只出现一次的字符是T。
'''
import sys

class CharStatistics(object):

    def __init__(self):
        self.char_appears = [-1] * 256
        self.index = 0
    
    def insert(self, char):

        if char is None or ord(char) >= 256:
            raise ValueError('char ascii must be between 0 and 255')

        if self.char_appears[ord(char)] == -1:
            self.char_appears[ord(char)] = index
        else:
            self.char_appears[ord(char)] = -2

        index += 1

    def appeared_once(self):

        min_idx = sys.maxsize
        ret = None
        for i in range(len(self.char_appears)):

            if self.char_appears[i] >= 0 and self.char_appears[i] < min_idx:
                min_idx = self.char_appears[i]
                ret = ord(i)
        return ret

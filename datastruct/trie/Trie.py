class Node(object):

        def __init__(self, is_word=False):
            self.next = {}
            self.is_word = is_word

class Trie(object):

    def __init__(self):
        self.__root = Node()
        self.__size = 0

    def get_size(self):
        return self.__size

    def add(self, word:str):
        '''
            向 Trie 中添加单词 word
        '''
        cur = self.__root
        for c in word:
            if(cur.next.get(c) is None):
                cur.next.update({c:Node()})
            cur = cur.next.get(c)
        if cur.is_word == False:
            cur.is_word = True
            self.__size += 1

    def contain(self, word:str):
        '''
            查看 Trie 中是否包含单词 word
        '''
        cur = self.__root
        for c in word:
            if(cur.next.get(c) is None):
                return False
            cur = cur.next.get(c)
        return cur.is_word
    
    def is_prefix(self, prefix:str):
        '''
            查看 Trie 中是否有以 prefix 为前缀的单词
        '''
        cur = self.__root
        for c in prefix:
            if(cur.next.get(c) is None):
                return False
            cur = cur.next.get(c)
        
        return True

    
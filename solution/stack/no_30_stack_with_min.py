'''面试题30：包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
在该栈中，调用min、push及pop的时间复杂度都是O（1）。
-----------------
省时间就要花空间，只要一次最小一个变量存储，一直要最小，就要一个辅助结构存
'''

class StackWithMin(object):

    def __init__(self):
        self.__data = []
        self.__min_stack = []
        self.__size = 0

    def push(self, ele):
        self.__data.append(ele)
        if self.__size == 0:
            self.__min_stack.append(ele)
        else:    
            top = self.__min_stack[self.__size - 1]
            self.__min_stack.append(ele) if ele < top else self.__min_stack.append(top)
        self.__size += 1
        
    def pop(self):
        if self.__size == 0:
            raise ValueError('Can not pop empty stack')
        ret = self.__data.pop()
        self.__min_stack.pop()
        self.__size -= 1

        return ret

    def min(self):

        if self.__size == 0:
            raise ValueError('Empty stack has no minimum')
        return self.__min_stack[self.__size - 1]

    def get_size(self):
        return self.__size

if __name__ == '__main__':

    datas = [[1,2,3,4,5],[5,4,3,2,1],[1],[]]
    min_stack = StackWithMin()

    for data in datas:
        print(data)
        for x in data:
            min_stack.push(x)
        for i in range(min_stack.get_size()):
            num = min_stack.min()
            print('%d, %d' % (min_stack.pop(), num))
        
            
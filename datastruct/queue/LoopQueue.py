from Queue import Queue


class LoopQueue(Queue):

    def __init__(self, capacity: int = 10):

        self.__data = [None] * (capacity + 1)
        self.__front = 0
        self.__tail = 0
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__front == self.__tail

    def enqueue(self, ele):

        if (self.__tail + 1) % len(self.__data) == self.__front:
            self.__resize((len(self.__data) - 1) * 2)

        self.__data[self.__tail] = ele
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__size += 1

    def __resize(self, new_capacity: int):

        new_data = [None] * (new_capacity + 1)

        for i in range(self.__size):
            new_data[i] = self.__data[(i + self.__front) % len(self.__data)]
        self.__data = new_data
        self.__front = 0
        self.__tail = self.__size

    def dequeue(self):

        if self.__size == 0:
            raise IndexError('Cannot dequeue from an empty queue!')


        res = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % (len(self.__data))
        self.__size -= 1

        if self.__size < self.get_capacity() / 4:
            self.__resize(self.get_capacity() // 2)

        return res

    def get_front(self):
        return self.__data[self.__front]

    def __str__(self):

        bstr = 'LoopQueue size: %d, capacity: %d\n' % (self.__size, len(self.__data))
        bstr += 'front ['
        i = self.__front
        while i != self.__tail:
            bstr += '' + str(self.__data[i])

            if (i + 1) % len(self.__data) != self.__tail:
                bstr += ', '

            i = (i + 1) % len(self.__data)
        bstr += '] tail'
        return bstr

    def get_capacity(self):
        return len(self.__data) - 1

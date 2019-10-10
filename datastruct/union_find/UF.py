from abc import ABCMeta, abstractmethod

class UF(metaclass=ABCMeta):

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def union(self, p, q):
        pass

    @abstractmethod
    def is_connected(self, p, q):
        pass
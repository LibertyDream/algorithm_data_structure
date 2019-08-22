from abc import ABCMeta, abstractmethod

class Set(metaclass = ABCMeta):

    @abstractmethod
    def add(self, ele):
        pass

    @abstractmethod
    def remove(self, ele):
        pass

    @abstractmethod
    def contains(self, ele):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

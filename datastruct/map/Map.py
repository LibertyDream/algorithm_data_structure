from abc import ABCMeta, abstractmethod


class Map(metaclass=ABCMeta):

    @abstractmethod
    def contains(self, key):
        """映射中是否包含 key"""
        pass

    @abstractmethod
    def is_empty(self):
        """映射是否为空"""
        pass

    @abstractmethod
    def get_size(self):
        """映射大小"""
        pass

    @abstractmethod
    def add(self, key, value):
        """向映射添加新（key，value）对，如果 key 已存在，更新 value"""
        pass

    @abstractmethod
    def remove(self, key):
        """从映射中删除 key 所在的结点"""
        pass

    @abstractmethod
    def get(self, key):
        """获取 key 所对应的 value，否则返回 None"""
        pass

    @abstractmethod
    def set(self, key, value):
        """设置 key 对应值为 value"""
        pass

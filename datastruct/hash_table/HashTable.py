class HashTable(object):


    def __init__(self):
        self.__capacity = [53, 97,193,389,769,1543,3079,6151,12289,24593,49157,
        98317,196613,393241,786433,1572869,3145739,6291469,12582917,25165843,
            50331653,100663319,201326611,402653189,805306457,1610612741]
        self.__size = 0
        self.__capacity_index = 0
        self.__up_tolerance = 10
        self.__down_tolerance = 2
        self.__M = self.__capacity[self.__capacity_index]  # 查询表大小
        self.__hash_table = [{}] * self.__M

    def __hash(self, key):
        '''所有元素都当作32位正整数处理,而后计算哈希值'''
        return (hash(key) & 0x7fffffff) % self.__M

    def add(self,key,value):
        get_map = self.__hash_table[self.__hash(key)]
        if get_map.get(key) is None:
            get_map.update({key: value})
            self.__size += 1
        else:
            get_map.update({key: value})

        if self.__size >= self.__up_tolerance * self.__M and self.__capacity_index + 1 < len(self.__capacity):
            self.__capacity_index += 1
            self.__resize(self.__capacity[self.__capacity_index])

    def remove(self,key):
        ret = None
        get_map = self.__hash_table[self.__hash(key)]
        if get_map.get(key) is not None:
            ret = get_map.get(key)
            self.__size -= 1
        
        if self.__size < self.__down_tolerance * self.__M and self.__capacity_index > 0:
            self.__capacity_index -= 1
            self.__resize(self.__capacity[self.__capacity_index])
        return ret
        
        return self.__hash_table[self.__hash(key)].pop(key)

    def put(self,key,value):
        get_map = self.__hash_table[self.__hash(key)]
        if get_map.get(key) is None:
            raise KeyError("key %s is not found" % key)
        get_map.update({key:value})

    def get(self,key):
        return self.__hash_table[self.__hash(key)].get(key)

    def contains(self,key):
        return self.__hash_table[self.__hash(key)].get(key) is not None

    def __resize(self, new_size):
        new_hash_table = [{}] * new_size
        
        old_M = self.__M
        self.__M = new_size

        for i in range(old_M):
            get_map = self.__hash_table[i]
            for key in get_map.keys():
                new_hash_table[self.__hash(key)].update({key:get_map[key]})
        
        self.__hash_table = new_hash_table

    def get_size(self):
        return self.__size
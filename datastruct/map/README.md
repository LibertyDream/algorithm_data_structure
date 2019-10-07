## 映射

计算机中的映射大多类似于高中数学的单射，就是 `key:value` 形式的键值对，很多语言中将其直接定义为字典，即`词：释义`结构。和集合类似，映射也是一个高层封装的数据结构，重要的是接口，底层实现是多样的

```
Map<K,V>{
    # 向映射集中添加新的键值对
    add(k,v)
    
    # 删除键为k的键值对并返回value
    remove(k)
    
    # 是否包含键为k的键值对
    contain(k)
    
    # 返回键k对应的值value
    get(k)
    
    # 将键k的值设为v
    set(k,v)
    
    # 映射集是否为空
    isEmpty()
    
    # 映射集大小
    getSize()
}
```

本实例中实现了基于链表的 LinkedListMap 和基于二分搜索树的 BSTMap

```
LinkedListMap<K,V>{
    class Node{
        K key
        V value
        Node next
	}
	
	add(k,v)  O(n)
	get(k)  O(n)
	remove(k)  O(n)
	contain(k)  O(n)
	set(k,v)  O(n)
}

BSTMap<K,V>{
    class Node{
        K key
        V value
        Node left,right
	}
	
	add(k,v)  O(logn)
	get(k)  O(logn)
	remove(k)  O(logn)
	contain(k)  O(logn)
	set(k,v)  O(logn)
}
```
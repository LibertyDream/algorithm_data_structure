## 集合

计算机里的集合和数学里集合论的集合相同，最重要的特点是无序性、特异性。集合和栈类似，都是一个高层封装的接口类的数据结构，用户调用接口进行使用，而具体的数据结构底层实现方式是多种多样的。

定义集合接口如下：

```
Set<E>{
    
    #  添加元素E
    add(E)
    
    #  删除元素E
    remove(E)
    
    #  是否包含元素E
    contains(E)
    
    #  集合大小
    getSize()
    
    #  集合是否为空
    isEmpty()
}
```

本实例中分别构建了基于自己实现的二分搜索树 BST（不保留重复元素）的集合 BSTSet，基于自己实现的链表 LinkedList 的集合 LinkedListSet

```
LinkedListSet:
    add(E)   O(n)
    remove(E)  O(n)
    contains(E)  O(n)
    
BSTSet:
    add(E)  O(logn)
    remove(E)  O(logn)
    contains(E)  O(logn)
```
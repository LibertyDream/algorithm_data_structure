## 链表

上述三种线性结构——动态数组、队列和栈底层都是依托静态数组实现的，动态扩容依靠的是 resize() 操作，并不能算是真正意义上的动态数据结构。

链表算是实际意义上最简单的动态数据结构,不再需要考虑固定容量的问题，但也丧失了随机访问的能力。常见于引用（指针）和辅助其他数据结构的场景。

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-23_linked_list.png)

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-23_linked_list_1.png)

链表首先要定义“节点”：

```
class Node{
    E e;
    Node next;
    
    Node(e, next)
    Node(e)
    Node()
}
```

本实例中的链表结构如下：

```
class LinkedList<E>

    dummyHead  # 虚拟头结点
    size
    
    LinkedList()
    getSize()
    isEmpty()
    
    # 增
    addToIndex(index, e)  O(n)
    addToFirst(e)  O(1)
    addToLast(e)  O(n)
    
    # 删
    remove(index)  O(n)
    removeFirst()  O(1)
    removeLast()  O(n)
    removeEle(E)  O(n)
    
    # 改
    set(index, e)  O(n)
    
    # 查
    contain(e)  O(n)
```
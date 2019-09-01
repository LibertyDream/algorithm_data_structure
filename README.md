# 算法与数据结构

一些常见数据结构与算法的自行实现，数据结构有 Java 1.8、Python 3.6 两种实现。算法题使用 Python 3.6 作答

| 数据结构                                                     | JAVA                                                         | Python                                                       |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [数组](https://github.com/LibertyDream/algorithm_data_structure#数组) | [Array](./datastruct/array/Array.java)                       | [Array](./datastruct/array/Array.py)                         |
| [栈](https://github.com/LibertyDream/algorithm_data_structure#栈) | [ArrayStack](./datastruct/stack/ArrayStack.java),[LinkedListStack](./datastruct/stack/LinkedListStack.java) | [ArrayStack](./datastruct/stack/ArrayStack.py),[LinkedListStack](./datastruct/stack/LinkedListStack.py) |
| [队列](https://github.com/LibertyDream/algorithm_data_structure#队列) | [ArrayQueue](./datastruct/queue/ArrayQueue.java),[LoopQueue](./datastruct/queue/LoopQueue.java),[LinkedListQueue](./datastruct/queue/LinkedListQueue.java) | [ArrayQueue](./datastruct/queue/ArrayQueue.py),[LoopQueue](./datastruct/queue/LoopQueue.py),[LinkedListQueue](./datastruct/queue/LinkedListQueue.py) |
| [链表](https://github.com/LibertyDream/algorithm_data_structure#链表) | [LinkedList](./datastruct/linkedlist/LinkedList.java)        | [LinkedList](./datastruct/linkedlist/LinkedList.py)          |
| [二分搜索树](https://github.com/LibertyDream/algorithm_data_structure#二分搜索树) | [BST](./datastruct/BST/BST.java)                             | [BST](./datastruct/BST/BST.py)                               |
| [集合](https://github.com/LibertyDream/algorithm_data_structure#集合) | [BSTSet](./datastruct/set/BSTSet.java),[LinkedListSet](./datastruct/set/LinkedListSet.java) | [BSTSet](./datastruct/set/BSTSet.py),[LinkedListSet](./datastruct/set/LinkedListSet.py) |
| [映射](https://github.com/LibertyDream/algorithm_data_structure#映射) | [LinkedListMap](./datastruct/map/LinkedListMap.java),[BSTMap](./datastruct/map/BSTMap.java) |                                                              |

## 数组

数组最大的优点是快速查询，比如 `score[2]`。数组最好应用于“索引带有语意”的情况，但并非所有有语意的索引都适用于数组，比如身份证号。

挑战在于如何使用数组处理那些“索引不带语意”的情况？索引没有语意，如何表示“没有元素”？如何添加元素？如何删除元素？......

如何自行二次封装一个数组类呢？本实例是一个动态扩容的泛化数组。

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-03_array_structure.png)

```
class Array<T>：
    # 成员
    
    data[]  # 存放数据
    size  # 使用量，默认指向第一个没有存放元素的位置
    
    # 构造方法
    
    Array(capacity)  # 给定数组容量的构造方法
    Array(Array_object)  # 用数组对象初始化数组
    Array(T... datas)  # 输入序列进行初始化
    Array()
    
    # 方法
    
    resize()  # 扩容  O(n) 
    
        # 增
    addToLast(ele)  # 添加新元素至末尾  O(n)  均摊复杂度O(1)
    addToFirst(ele)  # 添加新元素至首位  O(n)
    addToindex(index, ele)  # 添加新元素至指定索引  O(n)
   	
        # 删
    removeByIndex(index)  # 删除指定位置处的元素  O(n)
    removeEle(ele)  # 删除第一个与ele相等的元素  O(n)
    removeAllEle(ele)  # 删除所有与ele相等的元素  O(n)
    removeFirst()  # 删除头元素  O(n)
    removeLast()  # 删除末位元素  O(n) 均摊复杂度O(1)
    
        # 改
    set(index, ele)  # 将index处的值设为ele  O(1)
    
        # 查
    get(index)  # 返回index处的元素值  O(1)
    contain(ele)  # 判断是否含有ele  O(n)
    find(ele)  # 返回第一处与ele相等的元素位置索引，否则返回-1  O(n)
    findAll(ele)  # 返回所有与ele相等的元素位置索引，否则返回null  O(n)
    isEmpty()  # 数组是否为空
    
```

## 栈

栈也是线性结构，特点是只能从同一端添加和删除元素，这一端通常称为栈顶。加入元素的过程称为入栈，取出元素的过程称为出栈。

**栈是一种后进先出（LIFO, Last In First Out）的数据结构**

栈在计算机世界里十分常见，比如撤销操作，程序调用时的系统栈。

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-12-stack.png)

```
Interface Stack<E>
    void push<E>  # 入栈
    E pop()  # 出栈
    E peek()  # 查看栈顶元素
    int getSize()  # 栈内元素数量
    boolean isEmpty()  # 栈是否为空
```

对于用户而言需要的接口并不复杂，但是栈的底层实现可以多种多样，本实例中通过规定接口，完成了基于自建数组 Array 的 ArrayStack，和自建链表 LinkedList（虚拟头结点） 的 LinkedListStack。

```
ArrayStack<E>
    void push(E)     O(1)  # 均摊
    E pop()          O(1)  # 均摊
    E peek()         O(1)
    int getSize()    O(1)
    boolean isEmpty  O(1)
    
LinkedListStack<E>
    void push(E)     O(1)
    E pop()          O(1)
    E peek()         O(1)
    int getSize()    O(1)
    boolean isEmpty  O(1)
```

## 队列

队列是另外一种常见的线性结构，特点是只能从一端(队尾）添加元素，只能从另一端（队首）取出元素。

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-13_queue.png)

队列是一种先进先出（FIFO, First In First Out)的数据结构，即先到先得。

```
Queue<E>
    void enqueue(E)  # 入队
    E dequeue()  # 出队
    E getFront()  # 查看队首元素
    int getSize()  # 查看队列大小
    boolean isEmpty()  # 判断队列是否为空
```

用户对于队列的接口需求稳定而不关心底层实现，故本实例中通过规定接口，复用 Array 实现一个 ArrayQueue。

```
ArrayQueue<E>
    void enqueue(E)    O(1)  # 均摊
    E dequeue()        O(n)
    E getFont()        O(1)
    int getSize()      O(1)
    boolean isEmpty    O(1)
```

可以看到 ArrayQueue 的出队操作耗费时间期望比较大，我们希望出队操作时间复杂度也是O(1)，所以有了循环队列

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-18_loopqueue.png)

```
LoopQueue<E>
    void enqueue(E)    O(1)  # 均摊
    E dequeue()        O(1)  # 均摊
    E getFont()        O(1)
    int getSize()      O(1)
    boolean isEmpty    O(1)
```

_有了链表基础后，设计实现了基于带有头尾双指针链表的队列 LinkedListQueue_

```
LinkedListQueue<E>
    void enqueue(E)    O(1)
    E dequeue()        O(1)
    E getFont()        O(1)
    int getSize()      O(1)
    boolean isEmpty    O(1)
```



## 链表

上述三种线性结构——动态数组、队列和栈底层都是依托静态数组实现的，动态扩容依靠的是 resize() 操作，并不能算是真正意义上的动态数据结构。

链表算是实际意义上最简单的动态数据结构,不再需要考虑固定容量的问题，但也丧失了随机访问的能力。常见于引用（指针）和辅助其他数据结构的场景。

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-23_linked_list.png)

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-23_linked_list_1.png)

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

## 二分搜索树

当脱离了线性结构，数据不再“排成一排”，一种更天然的组织结构就呼之欲出了——树结构。树结构一大特点是高效，而针对一些特定问题使用树结构更是有奇效。这里首先展示的是二分搜索树，后面会有更多延展的树型结构。

探讨二分搜索树首先要提到二叉树，顾名思义，二叉树“分两叉”，有左右两个连接点。其和链表一样也是动态数据结构，也需要设计节点。二叉树的天然递归性相较于链表更加突出。

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-31_tree_structure.png)

```
class Node{
    E e
    Node left
    Node right
}
```

二分搜索树相较于二叉树添加了一些条件：

* 每个节点的值**大于**其**左子树**所有节点的值
* 每个节点的值**小于**其**右子树**所有节点的值
* 每一棵子树都是二分搜索树
* 存储的元素要有可比较性

本实例中的二分搜索树不包含重复元素。

```
class BST<E extends Comparable<E>>{
    private class Node{}
    
    Node root  # 根节点
    int size  # 树的大小
    
    getSize()
    isEmpty()  # 判断树是否为空
    
    # 增
    add() O(logn)
        __addRecur()  # 递归实现
        __addNonRecur()  # 非递归实现
        
    # 查
    contains(e)  O(logn)
        __containsRecur()
        __containsNonRecur()
    min()  #  最小值  O(logn)
    max()  #  最大值  O(logn)
    
    # 删
    removeEle(e)  #  删除元素e  O(logn)
    removeMin()  #  删除最小值  O(logn)
    removeMax()  #  删除最大值  O(logn)
}
```

_注：上述算法时间复杂度是平均状态下，存在退化至 O(n) 的可能，更多内容参见 AVL 和红黑树部分_

遍历树中元素历来是树结构绕不过去的话题，最自然的前序遍历，有排序功能的中序遍历（针对二分搜索树而言），后序遍历。除了这种先一头扎下去的深度优先遍历思路，还有一种一层一层递进的广度优先遍历，即层序遍历。

```
class BST<E extends Comparable<E>>{
    # 前序遍历
    preOrder()
        __preOrderRecur()    #  递归
        __preOrderNonRecur()  #  模仿系统栈的非递归
        __preOrderNonRecur2()  #  教科书式的非递归
    
    # 中序遍历
    inOrder()
        __inOrderRecur()
        __inOrderNonRecur()
        __inOrderNonRecur2()
        
    # 后序遍历
    postOrder()
        __postOrderRecur()
        __postOrderNonRecur()
        __postOrderNonRecur2()
    
    # 层序遍历     
    levelOrder()
}
```

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

## 映射

计算机中的映射大多类似于高中数学的单射，就是 key:value 形式的键值对，很多语言中将其直接定义为字典，即`词：释义`结构。和集合类似，映射也是一个高层封装的数据结构，重要的是接口，底层实现是多样的

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


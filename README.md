# 算法与数据结构

一些常见数据结构与算法的自行实现，数据结构有 Java 1.8、Python 3.6 两种实现。算法题使用 Python 3.6 作答

| 数据结构        | JAVA                                                         | Python                                                       |
| :-------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [数组](## 数组) | [Array](./datastruct/array/Array.java)                       | [Array](./datastruct/array/Array.py)                         |
| [栈](## 栈)     | [ArrayStack](./datastruct/stack/ArrayStack.java)             | [ArrayStack](./datastruct/stack/ArrayStack.py)               |
| [队列](## 队列) | [ArrayQueue](./datastruct/queue/ArrayQueue.java),[LoopQueue](./datastruct/queue/LoopQueue.java) | [ArrayQueue](./datastruct/queue/ArrayQueue.py),[LoopQueue](./datastruct/queue/LoopQueue.py) |

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

对于用户而言需要的接口并不复杂，但是栈的底层实现可以多种多样，本实例中通过规定接口，完成了基于自建数组 Array 的 ArrayStack。

```
ArrayStack<E>
    void push(E)     O(1)  # 均摊
    E pop()          O(1)  # 均摊
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

可以看到ArrayQueue的出队操作耗费时间期望比较大，我们希望出队操作时间复杂度也是O(1)，所以有了循环队列

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-18_loopqueue.png)

```
LoopQueue<E>
    void enqueue(E)    O(1)  # 均摊
    E dequeue()        O(1)  # 均摊
    E getFont()        O(1)
    int getSize()      O(1)
    boolean isEmpty    O(1)
```


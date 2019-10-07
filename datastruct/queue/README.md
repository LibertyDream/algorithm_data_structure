## 队列

队列是另外一种常见的线性结构，特点是只能从一端(队尾）添加元素，只能从另一端（队首）取出元素。

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-13_queue.png)

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

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-18_loopqueue.png)

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


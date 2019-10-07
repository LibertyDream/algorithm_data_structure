## 栈

栈也是线性结构，特点是只能从同一端添加和删除元素，这一端通常称为栈顶。加入元素的过程称为入栈，取出元素的过程称为出栈。

**栈是一种后进先出（LIFO, Last In First Out）的数据结构**

栈在计算机世界里十分常见，比如撤销操作，程序调用时的系统栈。

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-12-stack.png)

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
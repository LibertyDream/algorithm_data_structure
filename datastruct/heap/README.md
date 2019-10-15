## 优先队列和堆

优先队列也是队列，与普通队列的区别在于后者遵循时序优先，先进先出，后进后出。优先队列的出队顺序和入队顺序无关，和优先级相关。

优先队列也是一个接口，可以有不同的底层实现。自然的可以尝试使用线性结构实现优先队列，但无论哪种形式都会有一个操作是 O(n）复杂度的

|              | 入队 | 出队 |
| ------------ | ---- | ---- |
| 普通线性结构 | O(1) | O(n) |
| 顺序线性结构 | O(n) | O(1) |

为了高效，就要使用堆这种数据结构了。堆本质上也是一棵树，最常见的是二叉树构成的二叉堆，准确的说是一棵特殊的满二叉树。满二叉树就是所有元素一层一层填充进树中，如果有空，一定是在右下角。下图是一个堆的例子

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-09-16_max_heap.png)

堆的性质是堆中任意一个结点的值都不大于其父结点的值。同时因为是满二叉树，堆可以使用线性数据结构存储，比如数组。当索引从 0 记起，任意一个结点 i 的左孩子的索引为 2\*i + 1, 右孩子为 2\*i + 2，其父结点索引为 （i - 1）/ 2。当索引从 1 记起，任意一个结点 i 的左孩子的索引为 2\*i, 右孩子为 2\*i + 1，其父结点索引为 i / 2。

本实例实现了一个最大堆 MaxHeap，使用自己实现的动态数组作为存储结构

```
MaxHeap<E>{
    Array data
    
    getSize()
    isEmpty()
    
    # 向堆中添加新元素
    add(e)  O(logn)
        siftUp()   # 上浮操作

    # 返回堆中最大值
    findMax()  
    
    # 返回堆中最大值并将其从堆内删除
    extractMax()  O(logn)
        siftDown()  # 下沉操作
    
    # 取出堆中最大值，并加入一个新元素
    replace(e)  
}
```

之后，以 MaxHeap 为基础实现了优先队列 PriorityQueue，因为优先队列也是队列，所以复用接口只修改逻辑即可

```
Queue<E>
    void enqueue(E)  # 入队
    E dequeue()  # 优先级最高的元素出队
    E getFront()  # 查看优先级最高的元素
    int getSize()  # 查看队列大小
    boolean isEmpty()  # 判断队列是否为空
```
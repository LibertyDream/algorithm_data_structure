# 算法与数据结构 ![process](https://img.shields.io/badge/process-building-yellow)

一些常见数据结构与算法的白板实现，数据结构有 Java 1.8、Python 3.6 两种实现。算法题使用 Python 3.6 作答

| 数据结构                                                     | JAVA                                                         | Python                                                       |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [数组](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/array) | [Array](./datastruct/array/Array.java)                       | [Array](./datastruct/array/Array.py)                         |
| [栈](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/stack) | [ArrayStack](./datastruct/stack/ArrayStack.java),[LinkedListStack](./datastruct/stack/LinkedListStack.java) | [ArrayStack](./datastruct/stack/ArrayStack.py),[LinkedListStack](./datastruct/stack/LinkedListStack.py) |
| [队列](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/queue) | [ArrayQueue](./datastruct/queue/ArrayQueue.java),[LoopQueue](./datastruct/queue/LoopQueue.java),[LinkedListQueue](./datastruct/queue/LinkedListQueue.java) | [ArrayQueue](./datastruct/queue/ArrayQueue.py),[LoopQueue](./datastruct/queue/LoopQueue.py),[LinkedListQueue](./datastruct/queue/LinkedListQueue.py) |
| [链表](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/linkedlist) | [LinkedList](./datastruct/linkedlist/LinkedList.java)        | [LinkedList](./datastruct/linkedlist/LinkedList.py)          |
| [二分搜索树](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/BST) | [BST](./datastruct/BST/BST.java)                             | [BST](./datastruct/BST/BST.py)                               |
| [集合](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/set) | [BSTSet](./datastruct/set/BSTSet.java),[LinkedListSet](./datastruct/set/LinkedListSet.java),[AVLSet](./datastruct/set/AVLSet.java) | [BSTSet](./datastruct/set/BSTSet.py),[LinkedListSet](./datastruct/set/LinkedListSet.py),[AVLSet](./datastruct/set/AVLSet.py) |
| [映射](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/map) | [LinkedListMap](./datastruct/map/LinkedListMap.java),[BSTMap](./datastruct/map/BSTMap.java),[AVLMap](./datastruct/map/AVLMap.java) | [LinkedListMap](./datastruct/map/LinkedListMap.py),[BSTMap](./datastruct/map/BSTMap.py),[AVLMap](./datastruct/map/AVLMap.py) |
| [优先队列和堆](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/heap) | [MaxHeap](./datastruct/heap/MaxHeap.java),[PriorityQueue](./datastruct/heap/PriorityQueue.java) | [MaxHeap](./datastruct/heap/MaxHeap.py),[PriorityQueue](./datastruct/heap/PriorityQueue.py),[IndexMaxHeap](./datastruct/heap/index_max_heap.py) |
| [线段树](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/segment_tree) | [SegmentTree](./datastruct/segment_tree/SegmentTree.java)    | [SegmentTree](./datastruct/segment_tree/SegmentTree.py)      |
| [Trie 字典树](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/trie) | [Trie](./datastruct/trie/Trie.java)                          | [Trie](./datastruct/trie/Trie.py)                            |
| [并查集](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/union_find) | [UnionFind](./datastruct/trie/UnionFind.java)                | [UnionFind](./datastruct/trie/UnionFind.py)                  |
| [AVL](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/avl) | [AVL](./datastruct/avl/AVL.java)                             | [AVL](./datastruct/avl/AVL.py)                               |
| [红黑树](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/red_black_tree) | [RBTree](./datastruct/red_black_tree/RBTree.java)            | [RBTree](./datastruct/red_black_tree/RBTree.py)              |
| [哈希表](https://github.com/LibertyDream/algorithm_data_structure/tree/master/datastruct/hash_table) | [HashTable](./datastruct/hash_table/HashTable.java)          | [HashTable](./datastruct/hash_table/HashTable.py)            |

### 算法

<details>
    <summary>排序</summary>

* [选择排序](./algorithm/sort/selection_sort.py)
* [插入排序](./algorithm/sort/insertion_sort.py)
* [冒泡排序](./algorithm/sort/bubble_sort.py)
* [归并排序](./algorithm/sort/merge_sort.py)
* [快速排序](./algorithm/sort/quick_sort.py)
* [三路快速排序](./algorithm/sort/quick_sort_three_ways.py)
* [堆排序](./algorithm/sort/heap_sort.py)

| 名称     | 时间复杂度 | 空间复杂度 | 原地排序 | 稳定排序 |
| -------- | ---------- | ---------- | -------- | -------- |
| 选择排序 | O(n^2)     | O(1)       | √        | √        |
| 插入排序 | O(n^2)     | O(1)       | √        | √        |
| 冒泡排序 | O(n^2)     | O(1)       | √        | √        |
| 归并排序 | O(nlogn)   | O(n)       | ×        | √        |
| 快速排序 | O(nlogn)   | O(logn)    | √        | ×        |
| 堆排序   | O(nlogn)   | O(1)       | √        | ×        |

​    </details>

<details>
    <summary>图论</summary>

- [稀疏图](./algorithm/graph_theory/sparse_graph.py)
- [稠密图](./algorithm/graph_theory/dense_graph.py)
- [深度优先遍历与连通分量](./algorithm/graph_theory/depth_first.py)
- [深度优先遍历与路径](./algorithm/graph_theory/path.py)
- [广度优先遍历与最短路径](./algorithm/graph_theory/breadth_first.py)
- [带权稀疏图](./algorithm/graph_theory/weighted_sparse_graph.py)
- [带权稠密图](./algorithm/graph_theory/weighted_dense_graph.py)
- [懒惰 Prim 与最小生成树](./algorithm/graph_theory/lazy_prim.py)
- [Prim](./algorithm/graph_theory/prim.py)
- [Kruskal 与最小生成树](./algorithm/graph_theory/kruskal.py)
- [Dijkstra与最短路径](./algorithm/graph_theory/dijkstra.py)
- [Bellman_Ford与最短路径](./algorithm/graph_theory/bellman_ford.py)

</details>

### 剑指offer

<details>
    <summary>面试题1～10</summary>

- [面试题2：实现Singleton模式](./solution/offer/no_2 _singleton.py)

</details>
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

## 算法

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

## 编程习题

### 剑指offer

<details>
    <summary>知识基础</summary>

- [面试题2：实现Singleton模式](./solution/design_mode/no_2_singleton.py)
- [面试题3：找出数组中重复的数字](./solution/array/no_3_duplicate_num.py)
- [面试题3-1：不修改数组找出重复的数字](./solution/array/no_3_2_duplicate_num_no_change.py)
- [面试题4：二维数组中的查找](./solution/array/no_4_search_in_two_dim_array.py)
- [面试题5：替换空格](./solution/string/no_5_replace_blank.py)
- [面试题6：从尾到头打印链表](./solution/linked_list/no_6_print_list_reversely.py)
- [面试题7：重建二又树](./solution/tree/no_7_construct_tree.py)
- [面试题8：二又树的下一个节点](./solution/tree/no_8_next_node.py)
- [面试题9：用两个栈实现队列](./solution/queue/no_9_two_stack_to_a_queue.py)
- [面试题9-1：用两个队列实现栈](./solution/stack/no_9_1_two_queue_to_stack.py)
- [面试题10：斐波那契数列](./solution/recur_loop/no_10_fibonacci.py)
- [面试题10-1：青蛙跳台阶问题](./solution/recur_loop/no_10_1_frog_step.py)
- [面试题11：旋转数组的最小数字](./solution/recur_loop/no_11_rotate_array.py)
- [面试题12：矩阵中的路径](./solution/recur_loop/no_12_path_in_matrix.py)
- [面试题13：机器人的运动范围](./solution/recur_loop/no_13_step_counts.py)
- [面试题14：剪绳子](./solution/dynamic_greedy/no_14_cut_rope.py)
- [面试题15-1：二进制中1的个数](./solution/bit_map/no_15_number_of_1.py)
- [面试题15-2：2的整数次幂判断](./solution/bit_map/no_15_2_integer_power.py)

</details>

<details>
    <summary>高质量代码：规范，完整，鲁棒</summary>

- [面试题16：数值的整数次方](./solution/bit_map/no_16_power.py)
- [面试题17：打印从1到最大的n位数](./solution/string/no_17_print_1_to_max_n.py)
- [面试题18-1：删除链表的节点](./solution/linked_list/no_18_1_delete_node_O1.py)
- [面试题18-2：删除链表中重复的节点](./solution/linked_list/no_18_2_delete_duplicate.py)
- [面试题19：正则表达式匹配](./solution/string/no_19_regular_match.py)
- [面试题20：表示数值的字符串](./solution/string/no_20_num_string.py)
- [面试题21：调整数组顺序使奇数位于偶数前面](./solution/array/no_21_swap_ord_even.py)
- [面试题22：链表中倒数第k个节点](./solution/linked_list/no_22_Kth_to_tail.py)
- [面试题23：链表中环的入口节点](./solution/linked_list/no_23_entry_of_loop.py)
- [面试题24：反转链表](./solution/linked_list/no_24_reverse_linked_list.py)
- [面试题25：合并两个排序的链表](./solution/linked_list/no_25_merge_sorted_list.py)
- [面试题26：树的子结构](./solution/tree/no_26_same_structure.py)

</details>

<details>
    <summary>解决问题的思路：画图、举例、分解子问题</summary>

- [面试题27：二叉树的镜像](./solution/tree/no_27_mirror_tree.py)
- [面试题28：对称的二叉树](./solution/tree/no_28_symmetrical_tree.py)
- [面试题29：顺时针打印矩阵](./solution/array/no_29_print_array_clockwise.py)
- [面试题30：包含min函数的栈](./solution/stack/no_30_stack_with_min.py)
- [面试题31：栈的压入、弹出序列](./solution/stack/no_31_push_pop_queue.py)
- [面试题32-1：从上到下打印二叉树](./solution/tree/no_32_1_up_to_down_print_oneline.py)
- [面试题32-2: 分行从上到下打印二叉树](./solution/tree/no_32_2_up_to_down_print_ln.py)
- [面试题32-3: 之字形打印二叉树](./solution/tree/no_32_3_Z_type_print.py)
- [面试题33：二分搜索树的后序遍历序列](./solution/tree/no_33_verify_BST_post_order_seq.py)
- [面试题34：二叉树中和为某一值的路径](./solution/tree/no_34_find_path.py)
- [面试题35：复杂链表的复制](./solution/linked_list/no_35_clone_complex_list.py)
- [面试题36：二叉搜索树与双向链表](./solution/tree/no_36_bst_to_linked_list.py)
- [面试题37：序列化二叉树](./solution/tree/no_37_ser_deser_bst.py)
- [面试题38：字符串的排列](./solution/string/no_38_permutation.py)

</details>

<details>
    <summary>时间和空间效率</summary>

- [面试题39：数组中出现次数超过一半的数字](./solution/array/no_39_more_than_half.py)
- [面试题40：最小的k个数](./solution/heap/no_40_least_nums.py)
- [面试题41：数据流中的中位数](./solution/heap/no_41_get_median.py)
- [面试题42：连续子数组的最大和](./solution/array/no_42_max_sum_subset.py)
- [面试题43：1~n整数中1出现的次数](./solution/string/no_43_nums_of_1.py)
- [面试题44：数字序列中某一位的数字](./solution/string/no_44_digit_at_index.py)
- [面试题45：把数组排成最小的数](./solution/string/no_45_min_combine.py)
- [面试题46：把数字翻译成字符串](./solution/string/no_46_num_translation.py)
- [面试题47：礼物的最大价值](./solution/dynamic_greedy/no_47_max_gift_value.py)
- [面试题48：最长不含重复字符的子字符串](./solution/dynamic_greedy/no_48_longest_substring.py)
- [面试题49：丑数](./solution/array/no_49_ugly_num.py)
- [面试题50-1：字符串中第一个只出现一次的字符](./solution/set_hash/no_50_1_first_appeared_once.py)
- [面试题50-2：字符流中第一个只出现一次的字符](./solution/set_hash/no_50_2_first_appeared_once_flow.py)
- [面试题51：数组中的逆序对](./solution/array/no_51_inverse_pairs.py)
- [面试题52：两个链表的第一个公共节点](./solution/linked_list/no_52_first_common_node.py)

</details>
## 二分搜索树

当脱离了线性结构，数据不再“排成一排”，一种更天然的组织结构就呼之欲出了——树结构。树结构一大特点是高效，而针对一些特定问题使用树结构更是有奇效。这里首先展示的是二分搜索树，后面会有更多延展的树型结构。

探讨二分搜索树首先要提到二叉树，顾名思义，二叉树“分两叉”，有左右两个连接点。其和链表一样也是动态数据结构，也需要设计节点。二叉树的天然递归性相较于链表更加突出。

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-31_tree_structure.png)

```
class Node{
    E e
    Node left
    Node right
}
```

二分搜索树相较于二叉树添加了一些条件：

- 每个节点的值**大于**其**左子树**所有节点的值
- 每个节点的值**小于**其**右子树**所有节点的值
- 每一棵子树都是二分搜索树
- 存储的元素要有可比较性

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
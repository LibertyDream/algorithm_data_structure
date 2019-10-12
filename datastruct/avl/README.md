# AVL

之前手写的二分搜索树存在着退化成为链表的可能。为了避免这种情况发生，改进升级为平衡二叉树，对于 AVL 树要求对任一结点，左右子树高度差不超过一。为此我们要记录结点高度，计算平衡因子（左右子树高度差）

相比于一般二分搜索树， AVL 为了保持平衡多了左旋和右旋操作，只影响添加和删除操作，其余项无影响。本实例中同时扩展的还有范型，从 `AVL<E>` 扩展为 `AVL<K,V>`，方便封装成其他数据结构，比如 Map 和 Set。

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-11_avl_rotation.png)

需要显示维持平衡的有四种情况

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-11_avl_ll.png)

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-11_avl_rr.png)

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-11_avl_lr.png)

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-11_avl_rl.png)
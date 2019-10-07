## 线段树

有时候人们并不关心单个具体值的情况，而是想要针对区间进行查询，并在区间上进行统计计算，比如最大值、最小值或者对区间内的值求和等等。有代表性的问题有区间染色问题，查询 2018 年注册用户中消费最高的用户，学习时间最长的用户等。线段树正是为了这种区间问题而生。

使用线段树目的有二：一是更新，更新区间内的某个值或是整个区间内的值，二是在区间上统计查询。区间窗口大小不变，里面的内容会变。线段树结构如图所示

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-09-27_segment_tree.png)

线段树可以使用多种类型方式存储，本实例中采用数组的形式。对于一个存有 n 个数据的线段树，大约需要开 4n 大小的数组进行存储，这样的数组可以视作一棵满二叉树，对于任意内部结点 i，其左孩子的索引为 2i+1，右孩子的索引为 2i+2。因为线段树窗口大小不变，所以选择静态数组即可。

```
interface Merger<E>{  # 通过融合器可以自定义线段树的功能
	merge(E a, E b)
}

class SegmentTree<E>{
	E[] data
	E[] tree # tree 容量是 data 的 4 倍
	Merger merger
	
	# 线段树大小
	getSize()
	
	# 查询 [i...j] 范围内的内容
	query(i, j)  O(logn)
	
	# 更新 index 处的值为 e
	update(index, e)  O(logn)
}
```


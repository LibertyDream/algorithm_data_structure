# 算法与数据结构

一些常见数据结构与算法的自行实现，数据结构有 Java 1.8、Python 3.6 两种实现。算法题使用 Python 3.6 作答

## 数组

数组最大的优点是快速查询，比如 `score[2]`。数组最好应用于“索引带有语意”的情况，但并非所有有语意的索引都适用于数组，比如身份证号。

挑战在于如何使用数组处理那些“索引不带语意”的情况？索引没有语意，如何表示“没有元素”？如何添加元素？如何删除元素？......

如何自行二次封装一个数组类呢？本实例是一个动态的泛化数组，

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
    
   		# 增
   	addToLast(ele)  # 添加新元素至末尾
   	addToFirst(ele)  # 添加新元素至首位
   	addToindex(index, ele)  # 添加新元素至指定索引
   	
   		# 删
   	removeByIndex(index)  # 删除指定位置处的元素
   	removeEle(ele)  # 删除第一个与ele相等的元素
   	removeAllEle(ele)  # 删除所有与ele相等的元素
   	removeFirst()  # 删除头元素
   	removeLast()  # 删除末位元素
    
    	# 改
    set(index, ele)  # 将index处的值设为ele
    
    	# 查
    get(index)  # 返回index处的元素值
    contain(ele)  # 判断是否含有ele
    find(ele)  # 返回第一处与ele相等的元素位置索引，否则返回-1
    findAll(ele)  # 返回所有与ele相等的元素位置索引，否则返回null
    
```




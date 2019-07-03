# 算法与数据结构

一些常见数据结构与算法的自行实现，使用 Java、python两种语言完成。算法题使用python作答

## 数组

数组最大的优点是快速查询，比如 `score[2]`。数组最好应用于“索引带有语意”的情况，但并非所有有语意的索引都适用于数组，比如身份证号。

挑战在于如何使用数组处理那些“索引不带语意”的情况？索引没有语意，如何表示“没有元素”？如何添加元素？如何删除元素？......

如何自行二次封装一个数组类呢？该实例中以`int`型作示例，没有模板化。

![]( https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-07-03_array_structure.png)

```
class Array：
    # 成员
    
    data[]  # 存放数据
    size  # 使用量，默认指向第一个没有存放元素的位置
    
    # 构造方法
    
    Array(capacity)  # 给定数组容量的构造方法
    Array(Array_object)  # 用数组对象初始化数组
    Array(int... datas)  # 输入序列进行初始化
    Array()
    
    # 方法
    
   		# 增
   	addToLast(ele)  # 添加新元素至末尾
   	addToFirst(ele)  # 添加新元素至首位
   	addToindex(index, ele)  # 添加新元素至指定索引
   	
    delete  # 删
    
    	# 改
    set(index, ele)
    
    	# 查
    get(index)
```




# 哈希表

哈希表就是将一些“键”转换成“索引”，方便我们在 O(1) 时间内访问数据，“键”可以是基本数据类型或是自定义的复合类型。哈希表的两个设计要点是哈希函数和哈希冲突的解决，良好设计的哈希函数可以使“索引”分布十分均匀。

哈希表的思想是空间换时间，在空间和时间上取得平衡。具体哈希函数的设计是十分专业的一类问题，甚至特定领域有特定的哈希函数生成办法。这里只说一个一般性的方法——都当作整型处理

- 整型

小范围正数直接使用，小范围负数偏移使用（-100～100 >> 0～200）

大整数取模使用，存在取舍，要具体问题具体分析。取模本身就意味着加剧哈希冲突和分布不均的可能性，其次取模代代表放弃了一些数据信息。一般选择模一个质数，可以按照数据规模[查表](https://planetmath.org/goodhashtableprimes)。

- 浮点型

内部依然是32或是64位的整数，只是解析成了浮点数。转成整型处理即可

- 字符串

字符串可以按照编码规则，转换成多项式求和的形式变成大整型。比如说26字母表，就可以视为用26进制表示法表示字符串

```
code = c * 26^3 + 0 * 26^2 + d * 26^1 + e * 26^0
```

具体问题不同进制数不同，同时多项式加和结果可能溢出所以添加取余操作，模数规则同上

```
hash(code)=( c * B^3 + o * B^2 + d * B^1 + e * B^0) % M
```

单独计算 $$B^n$$ 是十分费事的，所以做个变形

```
hash(code)=(((( c * B) + o) * B + d) * B + e ) % M
```

防止算子溢出，把取余操作放进去，得到最终形式
$$
hash(code)=((((c\%M)*B+o)\%M*B+d)\%M*B+e)\%M
$$

```java
int hash = 0
for(int i = 0; i < str.length(); i++)
	hash = (hash * B + str.charAt(i)) % M
```

- 复合类型

复合类型可以视为不同字符类型的拼接，设计好进制数，然后计算方法同上
$$
hash(date)=(((date.year\%M)*B+ date.month)\%M*B + date.day)\%M
$$
以上只是设计哈希函数的一般性方法中的一种，总的来说哈希函数有三个原则：

1. 一致性：如果`a==b`，`hash(a)==hash(b)`
2. 高效性：计算简单便捷
3. 均匀性：哈希值均匀分布

至于哈希冲突，一个典型的方法是链地址法，即每个位置存储的是一个查找表，底层实现各异，可以是链表也可以是红黑树等。

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-14_hash_trouble.png)

本实例中的哈希表实现了动态扩容。哈希表提高了效率，但牺牲了顺序性。

```
class HashTable<K,V>{
	add(k,v)  # 均摊复杂度 O(1)
	
	remove(k) #均摊复杂度 O(1)
	
	set(k,v) O(1)
	
	contain(k) O(1)
	
	get(k) O(1)
}
```


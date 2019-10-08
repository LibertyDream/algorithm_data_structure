# Trie 字典树

相较于搜索树和堆的二叉树形式，trie 是常用多叉树，通常只用于处理字符串，可以做到查询时间只与字符串长度相关而与数据量无关，也就是说在字符串处理上 trie 拥有 O(w) 级别的效率。其一般结构如下

![](https://raw.githubusercontent.com/LibertyDream/diy_img_host/master/img/2019-10-08_trie.png)

考虑到语境、语言不同，trie 中每个结点可能要指向若干个结点，所以不适合用静态结构存储指向关系。本实例中选择映射，具体讲是 TreeMap， 作为指向关系的存储结构。同时，在寻找下一个字符时，我们是已经知道了字符是什么才会前往字符结点，所以结点内不需要存储字符值。而字符串又常常存在衍生，前缀等关系，所以区别于一般到达叶子结点才算结束，trie 的结点需要一个标识表示到了该结点时是否已经构成了一个单词。

所谓有得必有失，trie 查询高效的代价就是得付出额外的空间成本，同时当 trie 很庞大，开辟存储指针的空间的时间消耗也不能小觑

```
class Trie{
    class Node{
        boolean isWord
        Map<char, Node> next
    }
	
	Node root
	int size
	
	# 获取 Trie 存储的单词数量
	getSize()
	
	# 向 Trie 中添加单词 word
	add(word)  O(w)
	
	# 查询 Trie 中是否包含单词 word
	contain(word)  O(w) 
	
	# 查询 Trie 中是否包含以 prefix 为前缀的单词
	isPrefix(prefix)  O(w)
	
}
```


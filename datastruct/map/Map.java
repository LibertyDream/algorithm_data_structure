public interface Map<K,V> {

    // 向映射集中添加新的键值对
    void add(K key, V value);

    // 删除键为 key 的键值对并返回 value
    V remove(K key);

    // 是否包含键为 key 的键值对
    boolean contain(K key);

    // 将键 key 的值设为 value
    void set(K key, V value);

    // 返回键 key 对应的值 value
    V get(K key);

    // 映射集大小
    int getSize();

    // 映射集是否为空
    boolean isEmpty();

}

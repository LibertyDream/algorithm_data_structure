public interface Set<E> {

    //  向集合添加元素e
    void add(E e);

    //  判断集合中是否存在元素e
    boolean contains(E e);

    //  获取集合大小
    int getSize();

    //  判断集合是否为空
    boolean isEmpty();

    //  从集合中删除元素e
    void remove(E e);
}

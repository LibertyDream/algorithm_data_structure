public interface Queue<E> {
    //  入队
    void enqueue(E ele);

    //  出队
    E dequeue();

    // 队列大小
    int getSize();

    //  队列是否为空
    boolean isEmpty();

    //  队首元素
    E getFront();
}

public interface Stack<E> {

    // 出栈
    E pop();

    // 入栈
    void push(E ele);

    // 栈大小
    int getSize();

    // 查看栈顶元素
    E peek();

    // 判断栈是否为空
    boolean isEmpty();
}

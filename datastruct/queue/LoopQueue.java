import java.util.Objects;

public class LoopQueue<E> implements Queue<E> {

    private E[] data;
    private int front; // 队首元素位置
    private int tail;  // 下一个被传入元素的位置
    private int size;  // 队列内元素个数

    public LoopQueue(int capacity){
        data = (E[])new Object[capacity + 1];  // 循环队列会浪费一个空间
    }

    public LoopQueue(){
        this(10);
    }

    @Override
    public boolean isEmpty(){
        return front == tail;
    }

    @Override
    public int getSize(){
        return size;
    }

    public int getCapacity(){
        return  data.length - 1;
    }

    @Override
    public void enqueue(E ele){

        if((tail + 1) % data.length == front)
            resize(getCapacity() * 2);

        data[tail] = ele;
        tail = (tail + 1) % data.length;
        size++;
    }

    @Override
    public E dequeue(){
        if(front == tail)
            throw new IllegalArgumentException("Cannot dequeue from empty queue!");

        E res = data[front];
        data[front] = null;

        front = (front + 1) % data.length;
        size--;
        if(size < getCapacity() / 4)
            resize(getCapacity() / 2);
        return res;

    }

    @Override
    public E getFront(){
        return data[front];
    }

    private void resize(int newCapacity){
        E[] newdata = (E[])new Object[newCapacity + 1];
        for(int i = 0; i < size; i++){
            newdata[i] = data[(i + front) % data.length];
        }
        front = 0;
        tail = size;
        data = newdata;
    }

    @Override
    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("LoopQueue size: %d, capacity: %d\n", size, getCapacity()));
        sb.append("front [");
        for(int i = front; i != tail; i = (i + 1) % data.length){
            sb.append(data[i]);

            if((i + 1) % data.length != tail)
                sb.append(", ");
        }
        sb.append("] tail");
        return  sb.toString();
    }
}

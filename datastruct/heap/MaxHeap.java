
public class MaxHeap<E extends Comparable<E>> {

    private Array<E> data;

    public MaxHeap(int capacity){
        data = new Array<>(capacity);
    }

    public MaxHeap(){
        data = new Array<> ();
    }

    // 通过 heapify 操作将一个数组整理成最大堆
    public MaxHeap(E[] arr){

        data = new Array<> (arr);
        for(int i = getParent(arr.length - 1); i >= 0; i--){
            siftDown(i);
        }
        
    }

    // 返回堆中元素个数
    public int getSize(){
        return data.getSize();
    }

    // 堆是否为空
    public boolean isEmpty(){
        return data.isEmpty();
    }

    // 完全二叉树表示下，返回给定索引所在结点的左孩子的索引
    private int getLeftChild(int index){
        return 2 * index + 1;
    }

    // 完全二叉树表示下，返回给定索引所在结点的右孩子的索引
    private int getRightChild(int index) {
        return 2 * index + 2;
    }

    // 完全二叉树表示下，返回给定索引所咋结点的父结点的索引
    private int getParent(int index) {
        if (index == 0) {
            throw new IllegalArgumentException("index-0 doesn't have parent");
        }
        return (index - 1) / 2;
    }

    // 向堆添加一个新元素
    public void add(E e){
        data.addToLast(e);
        siftUP(data.getSize() - 1);
    }

    // 上浮操作
    private void siftUP(int k){

        while( k > 0 && data.get(getParent(k)).compareTo(data.get(k)) < 0){
            data.swap(k, getParent(k));
            k = getParent(k);
        }

    }

    // 返回堆内最大值
    public E findMax(){
        if (data.getSize() == 0) {
            throw new IllegalArgumentException("Heap is empty");
        }
        return data.get(0);
    }

    // 返回对内最大值并从堆内删除
    public E extractMax(){

        E ret = findMax();

        data.swap(0, data.getSize() - 1);
        data.removeLast();
        siftDown(0);

        return ret;
    }

    // 下沉操作
    private void siftDown(int k){

        while (getLeftChild(k) < data.getSize()) {
            int j = getLeftChild(k);
            if(j + 1 < data.getSize() && data.get(j).compareTo(data.get(j + 1)) < 0)
                j++;
            if(data.get(j).compareTo(data.get(k)) < 0)
                break;
            data.swap(k, j);
            k = j;
        }
    }

    // 取出堆中最大值，并加入一个新元素
    public E replace(E e){
        E ret = findMax();
        data.set(0, e);
        siftDown(0);
        return ret;
    }
}

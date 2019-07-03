public class Array {

    private int size; // 数组使用量，指向第一个没有存储元素的位置
    private int data[]; // 存储数据

    /**
     * 指定容量的构造方法
     * @param capacity 数组容量
     */
    public Array(int capacity){
        data = new int[capacity];
        size = 0;
    }

    /**
     * 变长参数构造Array
     * @param datas 存储数
     */
    public Array(int... datas){
        data = datas;
        size = data.length;
    }

    /**
     * 使用Array对象初始化Array对象
     * @param a_array 被传入的数组对象
     */
    public Array(Array a_array){
        data = a_array.data;
        size = data.length;
    }

    /**
     *  空构造函数
     */
    public Array(){
        this(10);
    }


    /**
     * 获取数组大小
     * @return 数组当前元素个数
     */
    public int getSize() {
        return size;
    }

    /**
     * 获取数组最大容量
     * @return 数组容量
     */
    public int getCapacity(){
        return data.length;
    }

    /**
     * 向数组末尾添加新的元素
     * @param ele 追加元素
     */
    public void addToLast(int ele){

        addToIndex(size, ele);
    }

    /**
     * 向数组首位添加元素
     * @param ele 新首位元素
     */
    public void addToFirst(int ele){

        addToIndex(0, ele);
    }

    /**
     * 向指定位置添加元素
     * @param index 位置索引
     * @param ele 加入的新元素
     */
    public void addToIndex(int index, int ele){

        if(size == data.length)
            throw new IllegalArgumentException("add to index failed! Array is full.");

        if(index < 0 || index > size)
            throw new IllegalArgumentException("add to index failed! we want index >=0 and index <= size.");

        for(int i = size; i > index; i--)
            data[i] = data[i - 1];

        data[index] = ele;
        size++;
    }

    /**
     * 返回给定索引处的值
     * @param index 给定的索引
     * @return
     */
    public int get(int index){

        if(index < 0 || index > size - 1)
            throw new IllegalArgumentException("Get failed! Make sure index is legal.");

        return data[index];
    }

    /**
     * 将给定索引处的值替换为ele
     * @param index
     * @param ele
     */
    public void set(int index, int ele){
        if(index < 0 || index > size - 1)
            throw new IllegalArgumentException("Get failed! Make sure index is legal.");
        data[index] = ele;
    }

    @Override
    public String toString(){
        StringBuilder str = new StringBuilder();
        str.append(String.format("Array size:%d, capacity:%d\n", size, data.length));
        str.append("[");
        for (int i = 0; i < size; i++){
            str.append(data[i]);
            if(i != size - 1)
                str.append(", ");
        }
        str.append("]");
        return str.toString();
    }
}

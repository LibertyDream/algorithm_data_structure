public class Array {

    private int size; // 数组使用量
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
}

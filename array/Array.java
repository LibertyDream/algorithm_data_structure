import java.util.Objects;

public class Array<T> {

    private int size; // 数组使用量，指向第一个没有存储元素的位置
    private T data[]; // 存储数据

    /**
     * 指定容量的构造方法
     * @param capacity 数组容量
     */
    public Array(int capacity){
        data = (T[])new Object[capacity]; // Java 1.8 不支持 new T[]
        size = 0;
    }

    /**
     * 变长参数构造Array
     * @param datas 存储数
     */
    public Array(T... datas){
        data = (T[])new Object[2 * datas.length];
        size = datas.length;
        for(int i = 0; i < size; i++)
            data[i] = datas[i];
    }

    /**
     * 使用Array对象初始化Array对象
     * @param a_array 被传入的数组对象
     */
    public Array(Array<T> a_array){
        data = (T[])new Object[2 * a_array.size];
        size = a_array.size;
        for (int i = 0; i < size; i++){
            data[i] = a_array.data[i];
        }
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
    public void addToLast(T ele){

        addToIndex(size, ele);
    }

    /**
     * 向数组首位添加元素
     * @param ele 新首位元素
     */
    public void addToFirst(T ele){

        addToIndex(0, ele);
    }

    /**
     * 向指定位置添加元素
     * @param index 位置索引
     * @param ele 加入的新元素
     */
    public void addToIndex(int index, T ele){

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
     * @param index 索引位置
     * @return 存储值
     */
    public T get(int index){

        if(index < 0 || index > size - 1)
            throw new IllegalArgumentException("Get failed! Make sure index is legal.");

        return data[index];
    }

    /**
     * 判定数组是否包含给定值
     * @param ele 给定值
     * @return 判断结果，true or false
     */
    public boolean contain(T ele){
        for(int i = 0; i < size; i++){
            if(data[i].equals(ele))  // 泛型需要值比较，不是==的索引比较
                return true;
        }
        return false;
    }

    /**
     * 找到给定元素的位置，并返回索引，否则返回-1
     * @param ele 待查找值
     * @return 元素索引
     */
    public int find(T ele){
        int res = -1;

        for(int i = 0; i < size; i++){
            if(ele.equals(data[i])){
                res = i;
                break;
            }
        }

        return res;
    }

    /**
     * 以数组形式返回所有和给定元素值相等的值的索引，否则返回null
     * @param ele 待查找元素
     * @return 索引数组
     */
    public int[] findAll(T ele){

        Array<Integer> temp = new Array<>();

        for(int i = 0; i < size; i++){
            if(data[i].equals(ele)) {
                temp.addToFirst(i);
            }
        }

        if(temp.size != 0) {
            int[] res = new int[temp.size];
            for(int i = 0; i < temp.size; i++){
                res[i] = temp.data[i];
            }
            return res;
        }
        return null;
    }

    /**
     * 删除第一个与给定值相等的元素
     * @param ele 待删除值
     */
    public void removeEle(T ele){
        int index = find(ele);
        if(index != -1)
            removeByIndex(index);
    }

    /**
     * 删除所有和给定元素相等的值
     * @param ele 待删除值
     */
    public void removeAllEle(T ele){
        int[] index = findAll(ele);
        if(index != null)
            for(int i = 0; i < index.length; i++)
                removeByIndex(index[i]);
    }

    /**
     * 删除头元素，并返回其值
     * @return
     */
    public T removeFirst(){
        return removeByIndex(0);
    }

    /**
     * 删除末位元素，并返回其值
     * @return
     */
    public T removeLast(){
        return removeByIndex(size - 1);
    }

    /**
     * 删除给定位置的元素并返回元素值
     * @param index 位置索引
     * @return 元素值
     */
    public T removeByIndex(int index){
        if(index < 0 || index > size - 1)
            throw new IllegalArgumentException("remove failed! Index is illegal");

        T res = data[index];

        for(int i = index; i < size - 1; i++){
            data[i] = data[i + 1];
        }

        size--;
        data[size] = null; // loitering objects 游荡对象，并非必须有的语句，不是内存泄漏
        return res;
    }

    /**
     * 将给定索引处的值设置为给定值
     * @param index 索引位置
     * @param ele 赋值内容
     */
    public void set(int index, T ele){
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

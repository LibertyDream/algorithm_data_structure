public class LinkedList<E> {
    private class Node{
        E e;
        Node next;

        public Node(E e, Node next){
            this.e = e;
            this.next = next;
        }

        public Node(E e){
            this.e = e;
            this.next = null;
        }

        public Node(){
            this.e = null;
            this.next = null;
        }

        @Override
        public String toString(){
            return e.toString();
        }
    }

    private Node dummyHead;
    private int size;

    /**
     * 获取链表大小
     * @return
     */
    public int getSize(){
        return size;
    }

    /**
     * 判断链表是否为空
     * @return
     */
    public boolean isEmpty(){
        return size == 0;
    }
    public LinkedList(){
        dummyHead = new Node(null, null);
        size = 0;
    }

    /**
     * 添加新元素至链表头
     * @param e
     */
    public void addToFirst(E e){

        addToIndex(0, e);
    }

    public void addToLast(E e){
        addToIndex(size, e);
    }

    /**
     * 添加新元素至指定索引处，索引位于[0,size]
     * 不是常用方法，仅做练习
     * @param index
     * @param e
     */
    public void addToIndex(int index,E e){

        if(index < 0 || index > size)
            throw new IllegalArgumentException("Add failed. index should be in [0, size].");

        Node prev = dummyHead;
        for(int i = 0; i < index; i++)    // 注意辨别有无虚拟头结点时的边界变化
            prev = prev.next;
//           Node node = new Node(e);
//           node.next = prev.next;
//           prev.next = node;

        prev.next = new Node(e, prev.next);
        size++;
    }

    /**
     * 获取指定位置的元素，索引位于[0, size)
     * 不是常用方法，仅做练习
     * @param index
     * @return
     */
    public E get(int index){
        if(index < 0 || index >= size)
            throw new IllegalArgumentException("Get failed. index should be in [0, size).");

        Node cur = dummyHead.next;
        for(int i = 0; i < index; i++)
            cur = cur.next;
        return cur.e;
    }

    /**
     * 获取链表头部元素
     * @return
     */
    public E getFirst(){
        return get(0);
    }

    /**
     * 获取链表最后一个元素
     * @return
     */
    public E getLast(){
        return get(size - 1);
    }

    /**
     * 将指定索引处的元素设置为指定值
     * 方法不常用，仅做练习
     * @param index
     * @param e
     */
    public void set(int index, E e){
        if(index < 0 || index >= size)
            throw new IllegalArgumentException("Set failed. index should be in [0, size).");

        Node cur = dummyHead.next;
        for(int i = 0; i < index; i++)
            cur = cur.next;
        cur.e = e;
    }

    /**
     * 判断链表是否包含指定元素
     * @param e
     * @return
     */
    public boolean contain(E e){
        Node cur = dummyHead.next;
        while (cur != null){
            if(cur.e.equals(e))
                return true;
            cur = cur.next;
        }
        return false;
    }

    /**
     * 删除指定位置的元素
     * 不常用的方法，仅做练习
     * @param index
     * @return
     */
    public E remove(int index){
        if(index < 0 || index >= size)
            throw new IllegalArgumentException("Set failed. index should be in [0, size).");

        Node pre = dummyHead;
        for(int i = 0; i < index; i++)
            pre = pre.next;
        Node ret = pre.next;
        pre.next = ret.next;
        ret.next = null;

        size--;

        return ret.e;
    }

    /**
     * 从链表中删除所有元素值与e相等的节点
     * @param e
     */
    public void removeEle(E e){
        Node pre = dummyHead;
        while (pre.next != null){
            if (pre.next.e.equals(e)){
                Node del = pre.next;
                pre.next = del.next;
                del.next = null;
                size--;
            }else{
                pre = pre.next;
            }
        }
    }

    /**
     * 删除第一个元素
     * @return
     */
    public E removeFirst(){
        return remove(0);
    }

    /**
     * 删除最后一个元素
     * @return
     */
    public E removeLast(){
        return remove(size - 1);
    }

    @Override
    public String toString(){
        StringBuilder str = new StringBuilder();
        Node cur = dummyHead.next;
        while(cur != null){
            str.append(cur.e + "->");
            cur = cur.next;
        }
        str.append("null");
        return str.toString();
    }
}

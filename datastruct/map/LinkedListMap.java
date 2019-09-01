public class LinkedListMap<K,V> implements Map<K, V> {

    private class Node{
        public K key;
        public V value;
        public Node next;

        public Node(K key, V value, Node next) {
            this.key = key;
            this.next = next;
            this.value = value;
        }

        public Node(K key){
            this(key, null, null);
        }

        public Node(){
            this(null, null, null);
        }

        @Override
        public String toString() {
            return key.toString() + ":" + value.toString();
        }
    }

    private Node dummyHead;
    private int size;

    public LinkedListMap(){
        dummyHead = new Node();
        size = 0;
    }

    @Override
    public int getSize() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    // 辅助方法，获取键为 key 的节点
    private Node getNode(K key){

        Node cur = dummyHead.next;

        while(cur != null){
            if(cur.key.equals(key))
                return cur;
            cur = cur.next;
        }
        return null;
    }

    @Override
    public boolean contain(K key) {
        return getNode(key) != null;
    }

    @Override
    public V get(K key) {
        Node node = getNode(key);

        return node == null ? null: node.value;
    }

    @Override
    public void add(K key, V value) {
        Node cur = getNode(key);

        if(cur == null){
            dummyHead.next = new Node(key, value, dummyHead.next);
            size++;
        }else {
            cur.value = value;
        }
    }

    @Override
    public void set(K key, V value) {
        Node cur = getNode(key);

        if ( cur == null) {
            throw  new IllegalAccessError(key + " doesn't exist");
        }else {
            cur.value = value;
        }
    }

    @Override
    public V remove(K key) {
        Node pre = dummyHead;

        while (pre.next != null) {
            if (pre.next.key.equals(key)) {
                Node cur = pre.next;
                pre.next = cur.next;
                cur.next = null;
                size--;
                return cur.value;
            }
            pre = pre.next;
        }

        return null;
    }
}

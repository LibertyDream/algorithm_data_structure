public class BSTMap<K extends Comparable <K>, V> implements Map<K,V> {

    private class Node{
        public K key;
        public V val;
        public Node left;
        public Node right;

        public Node(K key, V val) {
            this.key = key;
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }

    private Node root;
    private int size;

    public BSTMap(){
        root = null;
        size = 0;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public int getSize() {
        return size;
    }

    // 向二分搜索树中添加元素（key，value）
    @Override
    public void add(K key, V value) {
        root = add(root, key, value);
    }

    // 向以 node 为根的二分搜索树添加元素（key，value），递归实现
    // 返回添加元素后的根结点
    private Node add(Node node, K key, V value) {

        if(node == null){
            size++;
            return new Node(key, value);
        }

        if(key.compareTo(node.key) > 0 )
            node.right = add(node.right, key, value);
        else if(key.compareTo(node.key) < 0)
            node.left = add(node.left, key, value);
        else // key.compareTo(node.key) == 0
            node.val = value;

        return node;
    }

    // 返回以 node 为根结点的二分搜索树中关键字为 key 的结点
    private Node getNode(Node node, K key){
        if(node == null)
            return null;

        if(key.compareTo(node.key) < 0)
            return getNode(node.left, key);
        else if(key.compareTo(node.key) > 0)
            return getNode(node.right, key);
        else // key.compareTo(node.key) == 0
            return node;
    }

    @Override
    public boolean contain(K key) {
        return getNode(root, key) != null;
    }

    @Override
    public V get(K key) {
        Node node = getNode(root, key);
        return node == null ? null : node.val;
    }

    @Override
    public void set(K key, V value) {
        Node node = getNode(root, key);

        if(node == null)
            throw new IllegalArgumentException(key + " doesn't exist!");

        node.val = value;
    }

    // 返回以 node 为根结点的二分搜索树中的最小节点
    private Node min(Node node){
        if(node == null)
            throw new IllegalArgumentException("Tree is empty!");

        while(node.left != null)
            node = node.left;

        return node;
    }

    // 从以 node 为根结点的二分搜索树中删除 key 所在的结点
    // 返回删除元素后的根结点
    private Node removeMin(Node node, K key){
        Node ret = min(node);
        while(node.left != ret)
            node = node.left;
        node.left = ret.right;
        size--;
        return ret;
    }

    @Override
    public V remove(K key) {
        Node node = getNode(root, key);
        if(node == null)
            return null;
        root = remove(root, key);

        return node.val;
    }

    // 从以 node 为根结点的二分搜索树中删除 key 所在的结点
    // 返回删除结点后的根结点
    private Node remove(Node node, K key) {

        if(key.compareTo(node.key) < 0){
            node.left = remove(node.left, key);
        }
        else if(key.compareTo(node.key) > 0){
            node.right = remove(node.right, key);
        }
        else{ // key.compareTo(node.key) == 0
            if(node.left == null){
                Node ret = node.right;
                node.right = null;
                size--;
                return ret;
            }
            else if(node.right == null){
                Node ret = node.left;
                node.left = null;
                size--;
                return ret;
            }
            else{
                Node ret = min(node.right);
                ret.right = removeMin(node.right, key);
                ret.left = node.left;
                node.left = null;
                node.right = null;
                return ret;
            }
        }
        return node;
    }
}

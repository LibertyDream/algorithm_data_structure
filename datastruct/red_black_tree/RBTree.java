public class RBTree<K extends Comparable <K>, V>{

    private static final boolean RED = true;
    private static final boolean BLACK = false;

    private class Node{
        public K key;
        public V val;
        public Node left;
        public Node right;
        public boolean color;

        public Node(K key, V val) {
            this.key = key;
            this.val = val;
            this.left = null;
            this.right = null;
            this.color = RED;
        }
    }

    private Node root;
    private int size;

    public RBTree(){
        root = null;
        size = 0;
    }


    public boolean isEmpty() {
        return size == 0;
    }


    public int getSize() {
        return size;
    }

    // 查看结点颜色，检测是否是3结点
    private boolean isRed(Node node) {
        if(node == null)
            return BLACK;
        return node.color;
    }

    // 向红黑树中添加元素（key，value）
    public void add(K key, V value) {

        root = add(root, key, value);
        root.color = BLACK;  // 根结点保持黑色
    }

    // 左旋转
    private Node leftRotate(Node node){

        Node right = node.right;
        Node rightMin = right.left;

        right.left = node;
        node.right = rightMin;

        right.color = node.color;
        node.color = RED;

        return right;
    }

    // 右旋转
    private Node rightRotate(Node node){

        Node left = node.left;

        node.left = left.right;
        left.right = node;

        left.color = node.color;
        node.color = RED;

        return left;
    }

    // 颜色反转
    private void flipColors(Node node){
        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;
    }

    // 向以 node 为根的红黑树添加元素（key，value），递归实现
    // 返回添加元素后的根结点
    private Node add(Node node, K key, V value) {

        if(node == null){
            size++;
            return new Node(key, value);
        }

        if(key.compareTo(node.key) > 0 )
            node.right = add(node.right, key, value);
        else
            node.left = add(node.left, key, value);

        // < / ^ flip
        if(isRed(node.right) && !isRed(node.left))
            node = leftRotate(node);

        if(isRed(node.left) && isRed(node.left.left))
            node = rightRotate(node);

        if(isRed(node.right) && isRed(node.left))
            flipColors(node);

        return node;
    }

    // 返回以 node 为根结点的红黑树中关键字为 key 的结点
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


    public boolean contain(K key) {
        return getNode(root, key) != null;
    }


    public V get(K key) {
        Node node = getNode(root, key);
        return node == null ? null : node.val;
    }


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

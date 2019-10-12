import	java.util.ArrayList;

public class AVL<K extends Comparable <K>, V>{

    private class Node{
        public K key;
        public V val;
        public Node left;
        public Node right;
        public int height;

        public Node(K key, V val) {
            this.key = key;
            this.val = val;
            this.left = null;
            this.right = null;
            this.height = 1;
        }
    }

    private Node root;
    private int size;

    public AVL(){
        root = null;
        size = 0;
    }


    public boolean isEmpty() {
        return size == 0;
    }


    public int getSize() {
        return size;
    }

    // 向 AVL 树中添加元素（key，value）
    public void add(K key, V value) {
        root = add(root, key, value);
    }

    // 获取结点高度
    private int getHeight(Node node){
        if(node == null)
            return 0;

        return node.height;
    }

    // 计算平衡因子
    private int getBalanceFactor(Node node){
        if(node == null)
            return 0;

        return getHeight(node.left) - getHeight(node.right);
    }

    // 右旋转操作
    private Node rightRotate(Node node){
        Node left = node.left;
        Node leftMax = left.right;

        left.right = node;
        node.left = leftMax;

        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));
        left.height = 1 + Math.max(getHeight(left.left), getHeight(left.right));

        return left;
    }

    // 左旋转操作
    private Node leftRotate(Node node){
        Node right = node.right;
        Node rightMin = right.left;

        right.left = node;
        node.right = rightMin;

        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));
        right.height = 1 + Math.max(getHeight(right.left), getHeight(right.right));

        return right;
    }

    // 向以 node 为根的 AVL 树添加元素（key，value），递归实现
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

        // 更新高度
        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));

        // 计算平衡因子
        int balanceFactor = getBalanceFactor(node);


        // LL，形如 /，右旋转。左子树最大值转到右子树最小值
        if(balanceFactor > 1 && getBalanceFactor(node.left) >= 0)
            return rightRotate(node);

        // RR，形如 \，左旋转。右子树最小值转到左子树最大值
        if(balanceFactor < -1 && getBalanceFactor(node.right) <= 0)
            return leftRotate(node);

        // LR，形如 <，先对左子树做左旋转，再对结点做右旋转
        if(balanceFactor >  1 && getBalanceFactor(node.left) < 0){
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // RL,形如 >, 先对右子树右旋转，再对结点左旋转
        if(balanceFactor < -1 && getBalanceFactor(node.right) > 0){
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

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

        Node retNode;
        if(key.compareTo(node.key) < 0){
            node.left = remove(node.left, key);
            retNode = node;
        }
        else if(key.compareTo(node.key) > 0){
            node.right = remove(node.right, key);
            retNode = node;
        }
        else{ // key.compareTo(node.key) == 0
            if(node.left == null){
                Node ret = node.right;
                node.right = null;
                size--;
                retNode = ret;
            }
            else if(node.right == null){
                Node ret = node.left;
                node.left = null;
                size--;
                retNode = ret;
            }
            else{
                Node ret = min(node.right);
                ret.right = remove(ret, key);
                ret.left = node.left;
                node.left = null;
                node.right = null;
                retNode = ret;
            }
        }

        if(retNode == null)
            return null;

        // 更新高度
        retNode.height = 1 + Math.max(getHeight(retNode.left), getHeight(retNode.right));

        // 计算平衡因子
        int balanceFactor = getBalanceFactor(retNode);


        // LL，形如 /，右旋转。左子树最大值转到右子树最小值
        if(balanceFactor > 1 && getBalanceFactor(retNode.left) >= 0)
            return rightRotate(retNode);

        // RR，形如 \，左旋转。右子树最小值转到左子树最大值
        if(balanceFactor < -1 && getBalanceFactor(retNode.right) <= 0)
            return leftRotate(retNode);

        // LR，形如 <，先对左子树做左旋转，再对结点做右旋转
        if(balanceFactor >  1 && getBalanceFactor(retNode.left) < 0){
            retNode.left = leftRotate(retNode.left);
            return rightRotate(retNode);
        }

        // RL,形如 >, 先对右子树右旋转，再对结点左旋转
        if(balanceFactor < -1 && getBalanceFactor(retNode.right) > 0){
            retNode.right = rightRotate(retNode.right);
            return leftRotate(retNode);
        }

        return retNode;
    }

    // 判断是否满足二分搜索树性质
    public boolean isBST(){
        ArrayList<K> keys = new ArrayList<> ();
        inOrder(root, keys);
        for(int i = 1; i < keys.size(); i++){
            if(keys.get(i - 1).compareTo(keys.get(i)) > 0)
                return false;
        }
        return true;
    }

    private void inOrder(Node node, ArrayList<K> keys){
        if(node == null)
            return;

        inOrder(node.left, keys);
        keys.add(node.key);
        inOrder(node.right, keys);
    }

    // 判断是否满足平衡二叉树
    public boolean isBalanced() {
        return isBalanced(root);
    }

    private boolean isBalanced(Node node){
        if(node == null)
            return true;

        int balanceFactor = getBalanceFactor(node);
        if(Math.abs(balanceFactor) > 1)
            return false;
        return isBalanced(node.left) && isBalanced(node.right);
    }
}

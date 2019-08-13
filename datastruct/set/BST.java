import javafx.util.Pair;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class BST<E extends Comparable<E>> {
    private class Node{
        public E e;
        public Node left,right;

        public Node(E ele){
            this.e = ele;
            this.left = null;
            this.right = null;
        }
    }

    private Node root;
    private int size;

    public BST(){
        root = null;
        size = 0;
    }

    // 获取树大小
    public int getSize() {
        return size;
    }

    // 判断树是否为空
    public boolean isEmpty(){
        return size == 0;
    }

    // 向树内添加元素
    public void add(E e){
        root = __addRecur(root, e);
//        root = __addNonRecur(root, e);
    }

    // 向node为根的树内添加元素e，递归实现
    // 返回插入新元素后的根节点
    private Node __addRecur(Node node, E ele){
        if(node == null){
            size++;
            return new Node(ele);
        }

        if(node.e.compareTo(ele) > 0)
            node.left = __addRecur(node.left, ele);
        else if(node.e.compareTo(ele) < 0)
            node.right = __addRecur(node.right, ele);

        return node;
    }

    // 向node为根的树内添加元素e，非递归实现
    // 返回插入新元素后的根节点
    private Node __addNonRecur(Node node, E ele){
        Node pre = node;
        Node root = node;
        int dir = -1;  // 向左子树移动为1，右子树移动为0

        while(true){
            if(node == null){
                if(dir == -1) {
                    root = new Node(ele);
                }
                else if(dir == 1){
                    pre.left = new Node(ele);
                }else{
                    pre.right = new Node(ele);
                }
                size++;
                return root;
            }
            else if(node.e.equals(ele))
                return root;
            else if (node.e.compareTo(ele) < 0 ){
                pre = node;
                node = node.right;
                dir = 0;
            }else{
                pre = node;
                node = node.left;
                dir = 1;
            }
        }
    }

    //  判断树内是否含有元素ele
    public boolean contains(E ele){
        return __containsRecur(root, ele);
    }

    //  判断以node为根的树内是否有元素ele,递归实现
    private boolean __containsRecur(Node node, E ele){
        if(node == null)
            return false;

        if(node.e.equals(ele))
            return true;
        else if (node.e.compareTo(ele) > 0) {
            return __containsRecur(node.left, ele);
        }else{  // node.e.compareTo(ele) < 0
            return __containsRecur(node.right, ele);
        }
    }

    //  判断以node为根的树内是否有元素ele,非递归实现
    private boolean __containsNonRecur(Node node, E ele){
        while (true){
            if(node == null)
                return false;
            else if(node.e.equals(ele))
                return true;
            else if(node.e.compareTo(ele) < 0)
                node = node.right;
            else
                node = node.left;
        }
    }

    //  前序遍历
    public void preOrder(){
//        System.out.println("前序遍历\n");
        __preOrderRecur(root);
//        System.out.println();
//        __preOrderNonRecur2(root);
    }



    // 前序遍历node为根的二分搜索树,递归实现
    private void __preOrderRecur(Node node){
        if (node == null) {
            return;
        }

        System.out.println(node.e);

        __preOrderRecur(node.left);
        __preOrderRecur(node.right);
    }


    //  中序遍历
    public void inOrder(){
//        System.out.println("中序遍历\n");
        __inOrderRecur(root);
//        System.out.println();
//        __inOrderNonRecur2(root);
    }

    //  中序遍历以node为根节点的二分搜索树，递归实现
    private void __inOrderRecur(Node node){
        if(node == null)
            return;

        __inOrderRecur(node.left);
        System.out.println(node.e);
        __inOrderRecur(node.right);
    }

    //  后序遍历
    public void postOrder(){
//        System.out.println("后序遍历\n");
        __postOrderRecur(root);
//        System.out.println();
//        __postOrderNonRecur2(root);
    }

    //  后序遍历以node为节点的二分搜索树，递归实现
    private void __postOrderRecur(Node node){
        if(node == null)
            return;

        __postOrderRecur(node.left);
        __postOrderRecur(node.right);
        System.out.println(node.e);
    }

    // 模仿系统栈的递归，给定两个命令
    // GOTO: 前往节点，VISIT:访问节点
    private enum Command{
        GOTO,VISIT
    }

    //  前序遍历node为根的二分搜索树，模拟系统栈方式的非递归实现
    private void __preOrderNonRecur(Node node){
        if(node == null)
            return;

        Stack<Pair<Command,Node>> stack = new Stack<>();
        stack.push(new Pair<>(Command.GOTO,node));

        while (!stack.isEmpty()){
            Pair<Command,Node> cur = stack.pop();
            if(Command.VISIT == cur.getKey()) {
                System.out.print(cur.getValue().e + " ");
            }
            else{
                if(cur.getValue().right != null)
                    stack.push(new Pair<>(Command.GOTO, cur.getValue().right));
                if(cur.getValue().left != null)
                    stack.push(new Pair<>(Command.GOTO, cur.getValue().left));
                stack.push(new Pair<>(Command.VISIT, cur.getValue()));
            }

        }
    }

    // 中序遍历node为根的二分搜索树，模仿系统栈方式的非递归实现
    private void __inOrderNonRecur(Node node){
        if(node == null)
            return;

        Stack<Pair<Command, Node>> stack = new Stack<>();
        stack.push(new Pair<>(Command.GOTO, node));
        while (!stack.isEmpty()){
            Pair<Command, Node> cur = stack.pop();
            if (Command.VISIT == cur.getKey()) {
                System.out.print(cur.getValue().e + " ");
            }else{
                if(cur.getValue().right != null)
                    stack.push(new Pair<>(Command.GOTO, cur.getValue().right));
                stack.push(new Pair<>(Command.VISIT, cur.getValue()));
                if(cur.getValue().left != null)
                    stack.push(new Pair<>(Command.GOTO, cur.getValue().left));
            }

        }
    }

    // 后序遍历node为根的二分搜索树，模仿系统栈方式的非递归实现
    private void __postOrderNonRecur(Node node){
        if(node == null)
            return;

        Stack<Pair<Command, Node>> stack = new Stack<>();
        stack.push(new Pair<>(Command.GOTO, node));
        while (!stack.isEmpty()){
            Pair<Command, Node> cur = stack.pop();
            if (Command.VISIT == cur.getKey()) {
                System.out.print(cur.getValue().e + " ");
            }else{
                stack.push(new Pair<>(Command.VISIT, cur.getValue()));
                if(cur.getValue().right != null)
                    stack.push(new Pair<>(Command.GOTO, cur.getValue().right));
                if(cur.getValue().left != null)
                    stack.push(new Pair<>(Command.GOTO, cur.getValue().left));
            }

        }
    }

    // 前序遍历node为根的二分搜索树，教科书式非递归实现
    private void __preOrderNonRecur2(Node node){
        Stack<Node> stack = new Stack<>();
        Node cur = node;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null){
                System.out.print(cur.e + " ");
                stack.push(cur);
                cur = cur.left;
            }
            if(!stack.isEmpty()){
                cur = stack.pop();
                cur = cur.right;
            }
        }
    }

    // 中序遍历node为根的二分搜索树，教科书式非递归实现
    private void __inOrderNonRecur2(Node node){
        Stack<Node> stack = new Stack<>();
        Node cur = node;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            if (!stack.isEmpty()) {
                cur = stack.pop();
                System.out.print(cur.e + " ");
                cur = cur.right;
            }
        }
    }

    // 后序遍历node为根的二分搜索树，教科书式非递归实现
    private void __postOrderNonRecur2(Node node){
        Stack<Node> stack = new Stack<>();
        Node cur = node;
        Node pre = null;
        while (cur != null || !stack.isEmpty()){
            while (cur != null){
                stack.push(cur);
                cur = cur.left;
            }
            if (!stack.isEmpty()) {
                cur = stack.pop();
                if(cur.right != null && pre != cur.right){
                    stack.push(cur);
                    cur = cur.right;
                }else{
                    System.out.print(cur.e + " ");
                    pre = cur;
                    cur = null;
                }
            }
        }
    }

    //  层序遍历
    public void levelOrder(){
        if(root == null)
            return;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node cur = queue.remove();

            System.out.print(cur.e + " ");

            if(cur.left != null)
                queue.add(cur.left);
            if(cur.right != null)
                queue.add(cur.right);
        }
    }

    //  返回二分搜索树的最小值
    public E min(){
        if(size == 0)
            throw new IllegalArgumentException("BST is empty");
        return  __min(root).e;
    }

    //  返回node为根的二分搜索树的最小节点
    private Node __min(Node node){
        if(node.left == null)
            return node;

        return __min(node.left);
    }

    //  返回二分搜索树的最大值
    public E max(){
        if(size == 0)
            throw new IllegalArgumentException("BST is empty");
        return  __max(root).e;
    }

    //  返回node为根的二分搜索树的最大节点
    private Node __max(Node node){
        if(node.right == null)
            return node;

        return __max(node.right);
    }

    //  删除二分搜索树最小节点
    public E removeMin(){
        E ret = min();
        root = __removeMin(root);
        return ret;
    }

    //  删除node为根的二分搜索树的最小节点
    //  返回删除最小节点后的根节点
    private Node __removeMin(Node node) {

        if(node.left == null){
            Node ret = node.right;
            node.right = null;
            size--;
            return ret;
        }

        node.left = __removeMin(node.left);
        return node;
    }

    //  删除二分搜索树最大节点
    public E removeMax(){
        E ret = max();
        root = __removeMax(root);
        return ret;
    }

    //  删除node为根的二分搜索树的最大节点
    //  返回删除最大节点后的根节点
    private Node __removeMax(Node node) {

        if(node.right == null){
            Node ret = node.left;
            node.left = null;
            size--;
            return ret;
        }

        node.right = __removeMax(node.right);
        return node;
    }

    //  从二分搜索树中删除指定元素e所在的节点
    public void removeEle(E e){
        root = __removeEle(root, e);
    }

    //  从以node为根的二分搜索树中删除元素e所在的节点
    //  返回删除元素后的根节点
    private Node __removeEle(Node node, E e){
        if (node == null) {
            return null;
        }
        if (e.compareTo(node.e) < 0) {
            node.left = __removeEle(node.left, e);
            return node;
        } else if (e.compareTo(node.e) > 0) {
            node.right = __removeEle(node.right, e);
            return node;
        }else{ //  e == node.e
            if (node.left == null) {
                Node ret = node.right;
                node.right = null;
                size--;
                return ret;
            }else if (node.right == null) {
                Node ret = node.left;
                node.left = null;
                size--;
                return ret;
            }else{
                //  被删除节点有左右两个子树
                //  找到比当前节点大的最小值，即右子树的最小值代替当前节点
                //      或者找到比当前节点小的最大值，即左子树的最大值代替当前节点
                Node ret = __min(node.right);
                ret.right = __removeMin(node.right);
                ret.left = node.left;
                node.left = node.right = null;
                return ret;
            }

        }
    }

    @Override
    public String toString(){
        StringBuilder str = new StringBuilder();
        __generateTree(root, 0, str);
        return str.toString();
    }

    //  打印以node为根节点，深度为depth的树
    private void __generateTree(Node node, int depth, StringBuilder str){
        if (node == null) {
            str.append(__generateDepth(depth) + "null\n");
            return;
        }

        str.append(__generateDepth(depth) + node.e + "\n");
        __generateTree(node.left, depth + 1, str);
        __generateTree(node.right, depth + 1, str);
    }


    private String __generateDepth(int depth){
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < depth; i++) {
            res.append("--");
        }
        return res.toString();
    }
}

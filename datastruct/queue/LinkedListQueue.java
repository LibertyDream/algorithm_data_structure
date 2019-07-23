public class LinkedListQueue<E> implements Queue<E> {
    private class Node{
        public E e;
        public Node next;

        public Node(){
            next = null;
            e = null;
        }

        public Node(E e){
            this.e = e;
            this.next = null;
        }

        public Node(E e, Node next){
            this.e = e;
            this.next = next;
        }

        @Override
        public String toString(){
            return e.toString();
        }
    }

    private Node head, tail;
    private int size;

    public LinkedListQueue(){
        head = null;
        tail = null;
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

    @Override
    public void enqueue(E ele) {
        if(tail == null){
            tail = new Node(ele);
            head = tail;
        }
        else{
            tail.next = new Node(ele);
            tail = tail.next;
        }
        size++;
    }

    @Override
    public E dequeue() {
        if (isEmpty()) {
            throw new IllegalArgumentException("Cannot dequeue from an empty queue!");
        }

        Node ret = head;
        head = head.next;
        ret.next = null;

        if (head == null) {
            tail = null;
        }
        size--;
        return ret.e;
    }

    @Override
    public E getFront() {
        if (isEmpty()) {
            throw new IllegalArgumentException("Cannot get element from an empty queue!");
        }

        return head.e;
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        str.append("Queue: front ");

        Node cur = head;
        while (cur != null) {
            str.append(cur + "->");
            cur = cur.next;
        }
        str.append("null tail");

        return str.toString();
    }
}

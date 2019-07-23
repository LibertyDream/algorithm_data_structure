public class LinkedListStack<E> implements Stack<E> {

    private LinkedList<E> list;

    public LinkedListStack(){
        list = new LinkedList<>();
    }

    @Override
    public int getSize() {
        return list.getSize();
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public E pop() {
        return list.removeFirst();
    }

    @Override
    public void push(E ele) {
        list.addToFirst(ele);
    }

    @Override
    public E peek() {
        return list.getFirst();
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        str.append("Stack: top ");
        str.append(list);
        return str.toString();
    }
}

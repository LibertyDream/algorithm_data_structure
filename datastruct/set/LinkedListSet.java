public class LinkedListSet<E> implements Set<E> {

    private LinkedList<E> linkedList;

    public LinkedListSet(){
        linkedList = new LinkedList<>();
    }

    @Override
    public int getSize() {
        return linkedList.getSize();
    }

    @Override
    public void remove(E e) {
        linkedList.removeEle(e);
    }

    @Override
    public void add(E e) {
        if (!linkedList.contain(e)) {
            linkedList.addToFirst(e);
        }
    }

    @Override
    public boolean isEmpty() {
        return linkedList.isEmpty();
    }

    @Override
    public boolean contains(E e) {
        return linkedList.contain(e);
    }
}

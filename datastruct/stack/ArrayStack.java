public class ArrayStack<E> implements Stack<E> {
    private Array<E> array;

    public ArrayStack(int capacity){
        array = new Array<>(capacity);
    }

    public ArrayStack(){
        array = new Array<>();
    }

    @Override
    public E pop() {
        return array.removeLast();
    }

    @Override
    public void push(E ele) {
        array.addToLast(ele);
    }

    @Override
    public int getSize(){
        return array.getSize();
    }

    @Override
    public boolean isEmpty(){
        return array.isEmpty();
    }

    @Override
    public E peek(){
        return array.getLast();
    }

    public int getCapacity(){
        return array.getCapacity();
    }

    @Override
    public String toString(){
        StringBuilder str = new StringBuilder();
        str.append("Stack: [");
        for (int i = 0; i < array.getSize(); i++ ){
            str.append(array.get(i));
            if(i != array.getSize() - 1)
                str.append(", ");
        }
        str.append("] top");
        return str.toString();
    }
}

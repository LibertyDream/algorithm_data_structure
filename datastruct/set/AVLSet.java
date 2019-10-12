public class AVLSet<K extends Comparable<K>> implements Set<K> {
    private AVL<K, Object> avl;

    public AVLSet(){
        avl = new AVL<>();
    }

    @Override
    public int getSize() {
        return avl.getSize();
    }

    @Override
    public boolean isEmpty() {
        return avl.isEmpty();
    }

    @Override
    public void add(K k) {
        if(avl.get(k) == null)
            avl.add(k, null);
    }

    @Override
    public boolean contains(K k) {
        return avl.contain(k);
    }

    @Override
    public void remove(K k) {
        avl.remove(k);
    }
}

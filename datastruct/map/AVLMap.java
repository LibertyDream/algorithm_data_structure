public class AVLMap<K extends Comparable <K>, V> implements Map<K,V>{
    private AVL<K,V> avl;

    public AVLMap(){
        avl = new AVL<>();
    }

    @Override
    public boolean isEmpty() {
        return avl.isEmpty();
    }

    @Override
    public boolean contain(K key) {
        return avl.contain(key);
    }

    @Override
    public V get(K key) {
        return avl.get(key);
    }

    @Override
    public int getSize() {
        return avl.getSize();
    }

    @Override
    public void add(K key, V value) {
        V val = avl.get(key);
        if(val != null)
            avl.set(key, val);
        else
            avl.add(key, value);
    }

    @Override
    public void set(K key, V value) {
        avl.set(key, value);
    }

    @Override
    public V remove(K key) {
        return avl.remove(key);
    }
}

import	java.util.TreeMap;

public class HashTable<K,V> { // 不需要 key 可比较

    private static final int[] capacity = {53, 97,193,389,769,1543,3079,6151,12289,24593,
            49157,98317,196613,393241,786433,1572869,3145739,6291469,12582917,25165843,
            50331653,100663319,201326611,402653189,805306457,1610612741};
    private static final int upperBound = 10;
    private static final int lowerBound = 5;
    private int capacityIndex = 0;
    private TreeMap<K,V>[] hashtable;
    private int size;
    private int M;

    public HashTable(){
        size = 0;
        this.M = capacity [capacityIndex];
        hashtable = new TreeMap[M];

        for(int i = 0; i < M; i++){
            hashtable [i] = new TreeMap<>();
        }
    }

    // 都视为整型，与给定质数取余
    private int hash(K key){
        return (key.hashCode() & 0x7fffffff) % M;
    }

    public int getSize() {
        return size;
    }

    public void add(K key, V val){
        TreeMap<K, V> map = hashtable [hash(key)];
        if(map.containsKey(key))
            map.put(key, val);
        else{
            map.put(key, val);
            size++;  // 别忘了维护大小
        }

        if(size >= upperBound * M && capacityIndex + 1 < capacity.length) {
            capacityIndex++;
            resize(capacity[capacityIndex]);
        }
    }

    public V remove(K key){
        TreeMap<K, V> map = hashtable [hash(key)];
        V ret = null;
        if(map.containsKey(key)) {
            ret = map.remove(key);
            size--;
        }

        if(size < lowerBound * M && capacityIndex - 1 >= 0) {
            capacityIndex--;
            resize(capacity[capacityIndex]);
        }

        return ret;
    }

    public void set(K key, V val){
        TreeMap<K, V> map = hashtable [hash(key)];
        if(!map.containsKey(key))
            throw new IllegalArgumentException(key + " doesn't exist.");
        map.put(key,val);
    }

    public boolean contains(K key){
        return hashtable [hash(key)].containsKey(key);
    }

    public V get(K key){
        return hashtable [hash(key)].get(key);
    }

    private void resize(int newSize){

        TreeMap<K,V>[] newHashTable = new TreeMap[newSize];
        for(int i = 0; i < newSize; i++){
            newHashTable[i] = new TreeMap<> ();
        }

        int oldM = M;
        this.M = newSize;

        for(int i = 0; i < oldM; i++){
            TreeMap<K,V> map = hashtable[i];
            for(K key : map.keySet()){
                newHashTable[hash(key)].put(key, map.get(key));
            }
        }

        this.hashtable = newHashTable;
    }
}

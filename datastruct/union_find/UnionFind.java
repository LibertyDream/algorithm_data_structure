
public class UnionFind implements UF {

    private int[] parent; // 存储元素 i 父结点的索引
    private int[] rank; // 以索引 i 为根的树的深度

    public UnionFind(int size){
        parent = new int [size];
        rank = new int[size];
        for(int i = 0; i < size; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    @Override
    public int getSize() {
        return parent.length;
    }

    // 找到 index 所在集合的根结点
    private int find(int index){
        if(index < 0 || index >= parent.length)
            throw new IndexOutOfBoundsException("Index is out of bound");

        while(index != parent[index]) {
            parent[index] = parent[parent[index]];
            index = parent[index];
        }
        // 另一种路径压缩，通过递归实现将本次查询路径高度压缩为 2
//        if(index != parent[index]) {
//            parent[index] = find(parent[index]);
//        }
        return index;
    }

    // 判断 p，q 是否在一个集合内
    @Override
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }

    // 合并 p，q 所在集合
    @Override
    public void union(int p, int q) {
        int pRoot = find(p);
        int qRoot = find(q);

        if(pRoot == qRoot)
            return;

        if(rank[pRoot] < rank[qRoot]){
            parent[pRoot] = qRoot;
        } else if (rank[qRoot] < rank[pRoot]) {
            parent [qRoot] = pRoot;
        } else {
            parent[qRoot] = pRoot;
            rank[pRoot] += 1;
        }

    }
}

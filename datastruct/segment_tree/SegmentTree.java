public class SegmentTree<E> {

    private E[] data;
    private E[] tree;
    private Merger<E> merger; //融合器，自定义左右孩子的融合规则

    public SegmentTree(E[] arr, Merger<E> merger) {
        data = (E[])new Object [arr.length];
        for (int i = 0 ; i < arr.length; i++){
            data[i] = arr [i];
        }
        tree = (E[]) new Object[4 * arr.length];
        this.merger = merger;
        buildSegmentTree(0, 0, data.length - 1);
    }

    // 在 rootIndex 的位置创建 [left,right]范围内的线段树
    private void buildSegmentTree(int rootIndex, int left, int right) {

        if(left == right){
            tree[rootIndex] = data [left];
            return;
        }

        int mid = left + (right - left) / 2;
        int leftIndex = leftChild(rootIndex);
        int rightIndex = rightChild(rootIndex);
        buildSegmentTree(leftIndex, left, mid);
        buildSegmentTree(rightIndex, mid + 1, right);

        // 融合逻辑
        tree[rootIndex] = merger.merge(tree[leftIndex], tree[rightIndex]);
    }

    public E get(int index) {

        if (index < 0 || index >= data.length) {
            throw new IndexOutOfBoundsException("Index is illegal");
        }

        return data[index];
    }

    public int getSize(){
        return data.length;
    }

    private int leftChild(int index){
        return 2 * index + 1;
    }

    private int rightChild(int index) {
        return 2 * index + 2;
    }

    // 查询位于[queryL,queryR]范围内的内容
    public E query(int queryL, int queryR){
        if(queryL < 0 || queryL > data.length - 1
        || queryR < 0 || queryR > data.length - 1 || queryL > queryR){
            throw new IllegalArgumentException("Index queryL or queryR is illegal.");
        }

        return query(0, 0, data.length - 1, queryL, queryR);
    }

    // 查询以 treeIndex 为根，[left,right] 为界，目标范围为 [queryL,queryR] 中的内容
    private E query(int treeIndex, int left, int right, int queryL, int queryR){

        if(left == queryL && right == queryR){
            return tree[treeIndex];
        }

        int mid = left + (right - left) / 2;
        int leftIndex = leftChild(treeIndex);
        int rightIndex = rightChild(treeIndex);
        if(queryL >= mid + 1)
            return query(rightIndex, mid+1, right, queryL, queryR);
        if(queryR <= mid)
            return query(leftIndex,  left, mid, queryL, queryR);

        E leftRes = query(leftIndex, left, mid, queryL, mid);
        E rightRes = query(rightIndex, mid + 1, right, mid + 1, queryR);

        return merger.merge(leftRes, rightRes);
    }


    // 将 index 位置的元素更新为 e
    public void set(int index, E e){
        if (index < 0 || index > data.length - 1) {
            throw new IllegalArgumentException("Index is illegal.");
        }
        data [index] = e;
        set(0, 0, data.length - 1, index, e);
    }

    // 在以 treeIndex 为根的 [left,right] 的区间内更新 index 处的值为 e
    private void set(int treeIndex, int left, int right, int index, E e){

        if(left == right){
            tree [treeIndex] = e;
            return;
        }

        int mid = left + (right - left) / 2;
        int leftIndex = leftChild(treeIndex);
        int rightIndex = rightChild(treeIndex);

        if( index <= mid)
            set(leftIndex, left, mid, index, e);
        else // index >= mid + 1
            set(rightIndex, mid + 1, right, index, e);

        tree[treeIndex] = merger.merge(tree[leftIndex], tree[rightIndex]);
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        str.append("[");
        for (int i = 0; i < tree.length; i++) {
            if(tree[i] != null){
                str.append(tree[i]);
            }
            else{
                str.append("null");
            }

            if (i != tree.length - 1) {
                str.append(", ");
            }
        }
        str.append("]");

        return str.toString();
    }
}

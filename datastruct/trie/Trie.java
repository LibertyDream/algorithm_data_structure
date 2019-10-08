import java.util.TreeMap;

public class Trie {
    private class Node{
        boolean isWord;
        TreeMap<Character, Node> next;

        public Node(){
            this(false);
        }

        public Node(boolean isWord){
            this.isWord = isWord;
            next = new TreeMap<> ();
        }
    }

    private Node root;
    private int size;

    public Trie() {
        root = new Node();
        size = 0;
    }

    // 获得 Trie 中存储的单词数量
    public int getSize() {
        return size;
    }

    // 向 Trie 中添加新的单词
    public void add(String word){
        Node cur = root;
        for(int i = 0; i < word.length();i++){
            char c = word.charAt(i);
            if (cur.next.get(c) == null)
                cur.next.put(c, new Node());
            cur = cur.next.get(c);
        }

        if(!cur.isWord){
            cur.isWord = true;
            size++;
        }

    }

    // 查询 Trie 中是否包含单词 word
    public boolean contains(String word){
        Node cur = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (cur.next.get(c) == null) {
                return false;
            }
            cur = cur.next.get(c);
        }

        return cur.isWord;
    }

    // 查询 Trie 中是否包括以 prefix 为前缀的单词
    public boolean isPrefix(String prefix){
        Node cur = root;
        for(int i = 0; i < prefix.length(); i++){
            char c = prefix.charAt(i);
            if(cur.next.get(c) == null)
                return false;
            cur = cur.next.get(c);
        }
        return true;
    }

}

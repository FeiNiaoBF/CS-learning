/**
 * 单链表---整数类型
 */
public class SLList {
    public static class IntNode {
        public int date;
        public IntNode nxet;

        public IntNode(int x, IntNode L) {
            this.date = x;
            this.nxet = L;
        }

    }

    private IntNode head;
    private int size;

    public SLList() {
        size = 0;
        this.head = new IntNode(size, null);
    }

    public SLList(int x) {
        this.head = new IntNode(x, null);
        this.size = 1;
    }

    // 头插法
    public void addHead(int x) {
        IntNode newnode = new IntNode(x, null);
        newnode.nxet = this.head.nxet;
        this.head.nxet = newnode;
        this.size++;
    }

    public int getHead() {
        return this.head.date;
    }

    // 尾插法
    public void addTail(int x) {
        IntNode newNode = new IntNode(x, null);
        IntNode temp = this.head;
        while (temp.nxet != null) {
            temp = temp.nxet;
        }
        temp.nxet = newNode;
        this.size++;
    }

    // 长度

    public int size() {
        return size;
    }

    public static void main(String[] args) {
        SLList L = new SLList();
        // L.addHead(5);
        L.addTail(15);
        L.addTail(20);
        System.out.println(L.size());
    }

}

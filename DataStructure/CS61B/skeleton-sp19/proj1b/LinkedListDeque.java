import org.w3c.dom.Node;

/**
 * CS61B-pro1a
 * Array bacis List
 * 
 * @author Yeelight
 */

public class LinkedListDeque<T> {
    /* 双端节点类 */
    public class Node {
        /* 节点数据 */
        private T node;
        /* 节点的前端 */
        private Node prev;
        /* 节点的后继 */
        private Node next;

        /* 构造节点 */
        public Node(Node pPrev, T a, Node nNext) {
            node = a;
            prev = pPrev;
            next = nNext;
        }

        /* 指针节点 */
        public Node(Node pPrev, Node nNxet) {
            prev = pPrev;
            next = nNxet;
        }
    }

    /* 双端节点数据结构 */
    private Node pointerHead;
    private Node pointerTail;
    private int size;
    private int MAXNUM = 100;

    // 构造方法 使用双指针
    public LinkedListDeque() {
        pointerHead = new Node(null, null);
        pointerTail = new Node(pointerHead, null);
        pointerHead.next = pointerTail;
        size = 0;
    }

    /**
     * public void addFirst(T item)T：在双端队列的前面添加一个类型的项目。
     * public void addLast(T item)T：在双端队列的后面添加一个类型的项目。
     * public boolean isEmpty(): 如果 deque 为空，则返回 true，否则返回 false。
     * public int size()：返回双端队列中的项目数。
     * public void printDeque()：从头到尾打印双端队列中的项目，用空格分隔。打印完所有项目后，打印出一个新行。
     * public T removeFirst()：删除并返回双端队列前面的项目。如果不存在这样的项目，则返回 null。
     * public T removeLast()：删除并返回双端队列后面的项目。如果不存在这样的项目，则返回 null。
     * public T get(int index)：获取给定索引处的项目，其中 0 是前面，1 是下一个项目，依此类推。
     * 如果不存在这样的项目，则返回null。不能改变双端队列！
     * 
     */
    @Override
    public void addFirst(T item) {
        Node newnode = new Node(null, item, null);
        // 顺序不要乱，从后向前 ！！！不要把指向覆盖！！！
        this.pointerHead.next.prev = newnode;
        newnode.next = this.pointerHead.next;
        this.pointerHead.next = newnode;
        newnode.prev = this.pointerHead;
        size++;
    }

    @Override
    public void addLast(T item) {
        Node newnode = new Node(null, null);
        // 顺序不要乱，从前向后 ！！！不要把指向覆盖！！！
        this.pointerTail.prev.next = newnode;
        newnode.prev = this.pointerTail.prev;
        this.pointerTail.prev = newnode;
        newnode.next = this.pointerTail;
        size++;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public T removeFirst() {
        if (isEmpty()) {
            return null;
        }
        T couns = pointerHead.next.node;
        pointerHead.next.next.prev = pointerHead;
        pointerHead.next = pointerHead.next.next;
        size--;
        return couns;
    }

    @Override
    public T removeLast() {
        if (isEmpty()) {
            return null;
        }
        T couns = pointerTail.prev.node;
        pointerTail.prev.prev.next = pointerTail;
        pointerTail.prev = pointerTail.prev.prev;
        size--;
        return couns;
    }

    @Override
    public T get(int index) {
        if (index >= size) {
            return null;
        }
        Node temp = pointerHead;
        for (int i = 0; i <= index; i++) {
            temp = temp.next;
        }
        return temp.node;
    }

    /* 递归 */
    public T getRecursiveHelp(Node start, int index) {
        int x = 1;
        if (x == index) {
            return start.node;
        } else {
            return getRecursiveHelp(start.next, x++);
        }
    }

    public T getRecursive(int index) {
        if (index >= size) {
            return null;
        }
        return getRecursiveHelp(pointerHead.next, index);
    }

    @Override
    public void printDeque() {
        Node temp = pointerHead.next;
        while (temp != pointerTail) {
            System.out.println(temp.node);
            temp = temp.next;
        }
    }
}

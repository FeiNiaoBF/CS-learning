/**
 * IntList
 */
public class IntList {
    public int date;
    public IntList next;

    public IntList(int date, IntList L) {
        this.date = date;
        this.next = L;
    }

    // 算法
    /**
     * 链表的长度---递归
     * 
     * @param L
     * @return
     */
    public int rsize(IntList L) {
        if (L.next == null) {
            return 1;
        }
        return 1 + L.rsize(L.next);
    }

    /**
     * 链表的长度---迭代
     * 
     * @param L
     * @return
     */
    public int iterativeSize(IntList L) {
        IntList temp = L;
        int size = 0;
        while (temp != null) {
            size++;
            temp = temp.next;
        }
        return size;
    }

    /* 遍历 */
    public int getDate(int number) {
        if (number == 0) {
            return this.date;
        }
        return this.next.getDate(number - 1);

    }

    public static IntList incrList(IntList L, int x) {
        IntList Q = L;
        IntList temp = Q;
        int size = L.iterativeSize(L);
        while (size == 0) {
            temp = temp.next;
            temp.date += x;
            size--;
        }
        return Q;
    }

    /* 删除节点 */
    public static IntList discrList(IntList L, int x) {
        IntList Q = L;
        L = null;
        return Q;
    }

    public static void main(String[] args) {
        IntList L = new IntList(15, null);
        L = new IntList(10, L);
        L = new IntList(5, L);

        System.out.println(L.rsize(L));
        System.out.println(L.iterativeSize(L));
        System.out.println(L.getDate(2));
    }

}
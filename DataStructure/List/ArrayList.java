/**
 * Array based List
 * 
 * @author Yeelight
 */

/*
 * 数据结构：
 * -数组
 * -大小
 * -范围
 * 算法：
 * - 数组的插入
 * - 数组的遍历
 * - 数组的删除
 */

public class ArrayList {
    private int[] date;
    private int size;
    private int MAXNUM = 100;

    public ArrayList(int x) {
        date = new int[MAXNUM];
        size = 0;
    }

    public void addAList(int x) {
        if (size == date.length) {
            int[] A = new int[MAXNUM * 2];
            System.arraycopy(date, 0, A, 0, size);
            date = A;
        }
        date[size] = x;
        size++;
    }

    public int getAList(int x) {
        return date[x];
    }

    public int removeLastList() {
        int x = date[size - 1];
        date[size - 1] = 0;
        return x;
    }
}

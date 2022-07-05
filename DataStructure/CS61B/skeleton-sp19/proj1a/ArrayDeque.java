import java.io.PrintWriter;

import javax.lang.model.type.ArrayType;

/**
 * 基于数组的双端队列
 * 看成一个循环队列
 */

public class ArrayDeque<T> {
    private T[] array; // 数组本身
    private int size; // 大小
    private int lenght; // 总大小
    private int front; // 顶部指针
    private int rear; // 尾部指针

    public ArrayDeque() {
        this.array = (T[]) new Object[8];
        this.size = 0;
        this.lenght = 8;
        this.front = 4;
        this.rear = 4;
    }

    public ArrayDeque(ArrayDeque other) {
        ArrayDeque a = other;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    // 变更数组大小
    // 在后插法的时候用
    private int plusOne(int index, int len) {
        index %= len; // 防止溢出
        if (index == len - 1) {
            return 0;
        }
        return index + 1;
    }

    // 在前插法的时候用
    private int minusOne(int index) {
        if (index == 0) {
            return this.lenght - 1;
        }
        return index - 1;
    }

    private void growArray() {
        T[] newArray = (T[]) new Object[lenght * 2];
        int temp = front;
        int len = lenght;

        while (temp != rear) {
            newArray[len] = array[temp];
            temp = plusOne(temp, len);
        }

    }

    public void addFirst() {
        if (size == lenght - 1) {

        }
    }
}

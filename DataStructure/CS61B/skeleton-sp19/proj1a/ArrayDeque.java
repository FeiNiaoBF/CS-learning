/**
 * 基于数组的双端队列
 * 看成一个循环队列
 */

public class ArrayDeque<T> {
    private T[] array; // 数组本身
    private int lenght; // 总大小
    private int front; // 顶部指针
    private int rear; // 尾部指针
    private int maxObject = 8;

    public ArrayDeque() {
        this.array = (T[]) (new Object[maxObject]);
        this.lenght = maxObject;
        this.front = 0;
        this.rear = 0;
    }

    public void addFirst(T item) {
        if (isFull()) {
            reSize(maxObject * 2);
        }
        // 减一是因为要在数组中向前插入数值，而front要向前一位；
        // 对max进行取余则是让数组循环
        front = (front - 1 + maxObject) % maxObject;
        array[front] = item;
    }

    public void addLast(T item) {
        if (isFull()) {
            reSize(maxObject * 2);
        }
        array[rear] = item;
        rear = (rear + 1 + maxObject) % maxObject;
    }

    public int size() {
        return (rear - front + maxObject) % maxObject;
    }

    // boolen
    public boolean isEmpty() {
        return this.front == this.rear;
    }

    private boolean isFull() {
        return size() == maxObject - 1;
    }

    private boolean isLow() {
        return maxObject >= 16 && size() / (double) maxObject < 0.25;
    }

    // 变更数组大小
    private void reSize(int newSize) {
        T[] newArray = (T[]) (new Object[newSize]);

        int size = this.size();
        if (front < rear) {
            for (int i = front, j = 0; i < rear && j < size; i++, j++) {
                newArray[j] = array[i];
            }

        } else if (front > rear) {

            for (int i = rear, j = 0; i < maxObject && j < size; i++, j++) {
                newArray[j] = array[i];
            }
            for (int i = 0, j = 0; i < rear && j < size; i++, j++) {
                newArray[j] = array[i];
            }
            front = 0;
            rear = size;
            array = newArray;
            maxObject = newSize;
        }
    }

    // 删除数值
    // 节省空间，在大于25%的时候减少空间
    public T removeFirst() {
        if (isEmpty()) {
            return null;
        }
        T res = array[front];
        front = (front + 1 + maxObject) % maxObject;
        if (isLow()) {
            reSize((int) (maxObject * 0.25));
        }
        return res;
    }

    public T removeLast() {
        if (isEmpty()) {
            return null;
        }
        rear = (rear - 1 + maxObject) % maxObject;
        T res = array[rear];
        if (isLow()) {
            reSize((int) (maxObject * 0.25));
        }
        return res;
    }

    // 获取指定下标的值
    public T getDate(int index) {
        if (index < 0 || index >= size() || isEmpty()) {
            return null;
        }
        if (front < rear) {
            return array[index + front];
        } else if (front > rear) {
            return array[(index + front) % maxObject];
        }
        return null;
    }

    /*
     * 打印数值有两种情况
     * 1.当front的值小于rear时，此时应该从front开始到rear结束
     * 2.当rear的值小于front时，此时应该也从front开始但是要
     */

    public void printDeque() {
        if (front < rear) {
            for (int i = front; i < rear; i++) {
                if (i == rear - 1) {
                    System.out.println(array[i]);
                    break;
                }
                System.out.print(array[i] + " ");
            }

        } else if (front > rear) {
            for (int i = front; i < maxObject; i++) {
                System.out.print(array[i] + " ");
            }
            for (int i = 0; i < rear; i++) {
                if (i == rear - 1) {
                    System.out.println(array[i]);
                    break;
                }
                System.out.print(array[i] + " ");
            }
        }
    }

    public static void main(String[] args) {
        ArrayDeque<Integer> array = new ArrayDeque<>();
        array.addLast(2);
        array.addLast(4);
        array.addLast(6);
        array.addLast(15);
        array.printDeque();
    }
}

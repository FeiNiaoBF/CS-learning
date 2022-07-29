import org.junit.rules.DisableOnDebug;

/**
 * 要求如下：
 * 1、首先我们要有一个装bubble的二维数组，在其中'1'表示有'bubble'存在；'0'表示空格
 * 2、初始状态，所有泡泡都是“被黏住”（stuck）的。
 * 黏住的定义是：泡泡在最顶层（也就是grid[0]上），或者泡泡的主方向上存在被黏住的泡泡。
 * （学了个新词，orthogonally adjacent to，意思是主方向相邻）
 * 3、然后，向grid中的位置扔darts。
 * 4、darts也是二维数组，darts[i]代表第i个dart，里面存储了该dart的位置。
 * 如果dart所及位置是0，则没有任何改变；如果是1，则代表该处泡泡被"pop"，变为0；
 * 需要统计此时，有多少泡泡失去连接掉下来。返回一个数组存储了每次扔飞镖时掉落的泡泡。
 * 
 */
/**
 * 思路：
 * 1、有点像打气球，加上点三消的堆叠作用（在没有稳固的气泡时周围的气泡也将掉落）；
 * 2、要计算被打击的气泡，就要想清楚在打击气泡时剩余的气泡是否和顶部链接；
 */

public class BubbleGrid {

    private int[][] grid; // 气泡的位置；
    private int[][] direction = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };// 打标位置；
    private int row;
    private int col;
    private UnionFind unionBubble;

    // 构造函数
    public BubbleGrid(int[][] grid) {
        this.grid = grid;
        this.row = grid.length;
        this.col = grid[0].length;
        unionBubble = new UnionFind(row * col + 1);
    }

    /**
     * 二维数组转化为一维数组
     * 
     * @param x
     * @param y
     * @return
     */
    private int getIndex(int x, int y) {
        return x * col + y; // 行优先
    }

    /**
     * 判断是否超越gird
     * 
     * @param x
     * @param y
     * @return
     */
    private boolean inArray(int x, int y) {
        return x >= 0 && x < row && y >= 0 && y < col;
    }

    /**
     * 
     * @param darts
     * @return
     */

    // 主要函数
    public int[] popBubbles(int[][] darts) {
        // 对gird进行拷贝
        int[][] gridCoyp = new int[row][col];
        for (int i = 0; i < row; i++) {
            gridCoyp[i] = grid[i].clone();
        }
        // 把darts在gird的上的位置换为0
        for (int[] dart : darts) {
            gridCoyp[dart[0]][dart[1]] = 0;
        }
        // 建立图
        // 将二维数组最上面的一行和
        for (int j = 0; j < col; j++) {
            if (gridCoyp[0][j] == 1) {
                unionBubble.union(j, row * col);
            }
        }
        // 解决完最上的，就是到剩下的
        for (int i = 1; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (gridCoyp[i][j] == 1) {
                    // 如果该空间的上面是有气泡的，将要连接起来
                    if (gridCoyp[i - 1][j] == 1) {
                        unionBubble.union(getIndex(i - 1, j), getIndex(i, j));
                    }
                    // 如果该空间的左边是有气泡的，将要连结起来
                    if (gridCoyp[i][j - 1] == 1) {
                        unionBubble.union(getIndex(i, j - 1), getIndex(i, j));
                    }

                }
            }
        }
        // 开始补齐darts的位置
        int datrsSize = darts.length;
        int[] res = new int[datrsSize]; // 存储每一次因为补回而与顶相连的气泡的增量
        //
        for (int i = datrsSize - 1; i >= 0; i++) {
            int x = darts[i][0];
            int y = darts[i][1];
            // 发现此点是0时，跳出循环；
            if (grid[x][y] == 0) {
                continue;
            }
            // 发现此点是在最上行时，要和屋顶相连
            int origin = unionBubble.sizeOf(row * col); // 原来相连的点数
            if (x == 0) {
                unionBubble.union(y, row * col);
            }
            // 剩下的四周
            for (int[] directions : direction) {
                int dx = x + directions[0];
                int dy = y + directions[1];
                if (inArray(dx, dy) && gridCoyp[dx][dy] == 1) {
                    unionBubble.union(getIndex(x, y), getIndex(dx, dy));
                }
            }
            int current = unionBubble.sizeOf(row * col);
            res[i] = Math.max(0, current - origin - 1);
            gridCoyp[x][y] = 1;
        }
        return res;
    }
}

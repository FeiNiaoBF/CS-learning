import org.junit.Test;
import static org.junit.Assert.*;

public class TestUnionFind {

    UnionFind uf = new UnionFind(8);

    @Test
    public void testBasic() {
        assertEquals(-1, uf.parent(2));
        assertEquals(-1, uf.parent(0));
        assertEquals(1, uf.sizeOf(0));
        uf.union(0, 1);
        assertEquals(2, uf.sizeOf(1));
        assertEquals(1, uf.parent(0));
        uf.union(2, 3);
        assertEquals(3, uf.parent(2));
        uf.union(1, 2);
        assertEquals(1, uf.parent(0));
        assertEquals(3, uf.parent(1));

        assertTrue(uf.connected(0, 2));
        assertEquals(3, uf.parent(0)); // Path-compression
        assertEquals(3, uf.parent(2));
        assertEquals(3, uf.parent(1));
        assertEquals(4, uf.sizeOf(0));
        assertEquals(3, uf.find(0));
        assertFalse(uf.connected(1, 5));

        uf.union(5, 6);
        assertEquals(6, uf.parent(5)); // Path-compression

        uf.union(1, 5);
        assertEquals(6, uf.sizeOf(5));
        assertEquals(3, uf.find(5));
        assertTrue(uf.connected(1, 3));

    }

}
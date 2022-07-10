public class OffByN implements CharacterComparator {

    private int N;

    public OffByN(int n) {
        N = n;
    }

    public boolean equalChars(char x, char y) {
        int diff = x - y;
        return diff == this.N || diff == -this.N;
    }

}

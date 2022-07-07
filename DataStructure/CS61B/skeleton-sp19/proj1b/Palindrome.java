import java.util.ArrayDeque;
import java.util.Deque;

public class Palindrome {
    // 先把字符一一的向链表中插入
    public Deque<Character> wordToDeque(String word) {
        Deque<Character> res = new ArrayDeque<>();
        for (int i = 0; i < word.length(); i++) {
            res.addLast(word.charAt(i));
        }
        return res;
    }

    // 对是回文的单词进行判断
    public boolean isPalindrome(String word) {
        Deque<Character> db = wordToDeque(word);
        /* 1 or 0 都是回文字符 */
        while (db.size() > 1) {
            if (db.removeFirst() != db.removeLast()) {
                return false;
            }
        }
        return true;
    }

    public boolean isPalindrome(String word, CharacterComparator cc) {
        Deque<Character> d = wordToDeque(word);
        while (d.size() > 1) {
            if (!cc.equalChars(d.removeFirst(), d.removeLast())) {
                return false;
            }
        }
        return true;
    }
}

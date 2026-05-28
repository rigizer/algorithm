import java.util.*;

class Solution {
    boolean solution(String s) {
        Queue<Character> queue = new LinkedList();
        for (char c: s.toCharArray()) {
            queue.offer(c);
        }
        
        int i = 0;
        while (!queue.isEmpty()) {
            char c = queue.poll();
            if (c == '(') {
                i++;
            } else {
                i--;
            }
            
            if (i < 0) {
                return false;
            }
        }
        
        if (i != 0) return false;
        return true;
    }
}
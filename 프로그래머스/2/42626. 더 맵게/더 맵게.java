import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s: scoville) {
            pq.offer(s);
        }
        
        while (pq.peek() < K) {
            if (pq.size() <= 1) {
                return -1;
            }
            
            int x = pq.poll();
            int y = pq.poll();
            
            if (x == 0 && y == 0) {
                return -1;
            }
            
            pq.offer(x + (y * 2));
            answer++;
        }
        
        if (pq.poll() < K) {
            return -1;
        }
        
        return answer;
    }
}
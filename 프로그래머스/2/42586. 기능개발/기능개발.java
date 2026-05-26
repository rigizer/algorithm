import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = new int[100];
        int n = progresses.length;
        Queue<Integer> queue = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            int work = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            queue.offer(work);
        }
        
        int maxWork = queue.poll();
        int count = 1;
        int answerIdx = 0;
        
        while (!queue.isEmpty()) {
            int work = queue.poll();
            
            if (maxWork >= work) {
                count++;
            } else {
                answer[answerIdx++] = count;
                count = 1;
                maxWork = work;
            }
        }
        
        answer[answerIdx++] = count;
        
        return Arrays.copyOf(answer, answerIdx);
    }
}
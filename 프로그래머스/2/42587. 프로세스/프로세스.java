import java.util.*;

class Process {
    int number;      // 프로세스 고유번호(입력순서)
    int priority;    // 프로세스 우선순위
    
    public Process(int number, int priority) {
        this.number = number;
        this.priority = priority;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Process> queue = new LinkedList<>();
        
        int n = priorities.length;
        for (int i = 0; i < n; i++) {
            queue.offer(new Process(i, priorities[i]));
        }
        
        int result = 0;
        while (!queue.isEmpty()) {
            Process current = queue.poll();

            boolean hasHigher = false;

            for (Process process : queue) {
                if (process.priority > current.priority) {
                    hasHigher = true;
                    break;
                }
            }

            if (hasHigher) {
                queue.offer(current);
            } else {
                result++;

                if (current.number == location) {
                    return result;
                }
            }
        }

        return result;
    }
}
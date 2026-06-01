import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        for (int truck : truck_weights) {
            queue.offer(truck);
        }

        Queue<Integer> bridge = new LinkedList<>();
        int bridge_weight = 0;

        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }

        while (!queue.isEmpty()) {
            answer++;
            bridge_weight -= bridge.poll();

            if (bridge_weight + queue.peek() <= weight) {
                int truck = queue.poll();
                bridge.offer(truck);
                bridge_weight += truck;
            } else {
                bridge.offer(0);
            }
        }

        return answer + bridge_length;
    }
}
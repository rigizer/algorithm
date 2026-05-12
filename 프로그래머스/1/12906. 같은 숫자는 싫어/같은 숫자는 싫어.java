import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();
        int last = -1;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != last) {
                answer.add(arr[i]);
                last = arr[i];
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}
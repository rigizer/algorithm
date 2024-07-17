import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int count = 0;
        int computer = sc.nextInt();
        int connect = sc.nextInt();
        int[][] checked = new int[computer + 1][computer + 1];
        int[] visited = new int[computer + 1];  // 방문 여부를 저장하는 배열
        
        // 연결된 좌표 저장
        for (int i = 0; i < connect; i++) {
            int front = sc.nextInt();
            int rear = sc.nextInt();
            checked[front][rear] = 1;
            checked[rear][front] = 1; // 양방향 연결 설정
        }
        
        Deque<Integer> queue = new ArrayDeque<>();
        queue.add(1);
        visited[1] = 1; // 1번 컴퓨터 방문 처리
        
        while (!queue.isEmpty()) {
            int start = queue.pop();
            for (int end = 1; end <= computer; end++) {
                if (checked[start][end] == 1 && visited[end] == 0) { // 연결되어 있고 방문하지 않은 경우
                    queue.add(end);
                    visited[end] = 1; // 방문 처리
                    count++;
                }
            }
        }
        
        System.out.println(count);
    }
}
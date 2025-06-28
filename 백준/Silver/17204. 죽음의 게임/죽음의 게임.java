import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] next = new int[n];
        for (int i = 0; i < n; i++) {
            next[i] = sc.nextInt();
        }

        int current = 0;
        boolean[] visited = new boolean[n];

        for (int m = 1; m <= n + 1; m++) {
            current = next[current];
            if (current == k) {
                System.out.println(m);
                return;
            }
            
            if (visited[current]) break;
            visited[current] = true;
        }

        System.out.println(-1);
    }
}
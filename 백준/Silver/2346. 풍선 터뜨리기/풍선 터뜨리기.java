import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] balloon = new int[n];
        boolean[] visited = new boolean[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            balloon[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> list = new ArrayList<>();
        int i = 0;

        for (int count = 0; count < n; count++) {
            visited[i] = true;
            list.add(i + 1);

            if (count == n - 1) break;

            int move = balloon[i];
            int step = 0;

            if (move > 0) {
                while (step < move) {
                    i = (i + 1) % n;
                    if (!visited[i]) step++;
                }
            } else {
                while (step > move) {
                    i = (i - 1 + n) % n;
                    if (!visited[i]) step--;
                }
            }
        }

        list.forEach(idx -> System.out.print(idx + " "));
    }
}
import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] data;
    static boolean[] visited;
    static int[] path;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n];
        visited = new boolean[n];
        path = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(data);

        dfs(0);

        System.out.print(sb.toString());
    }

    static void dfs(int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(path[i]).append(' ');
            }
            sb.append('\n');
            return;
        }

        int prev = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            if (data[i] == prev) {
                continue;
            }

            visited[i] = true;
            path[depth] = data[i];
            prev = data[i];

            dfs(depth + 1);

            visited[i] = false;
        }
    }
}

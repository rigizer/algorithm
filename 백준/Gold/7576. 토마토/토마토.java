import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, 1, 0, -1};

    private static int bfs(int m, int n, int count, int[][] tomato) {
        if (count == 0) {
            return 0;
        }

        int day = 0;
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tomato[i][j] == 1) {
                    queue.offer(new int[] {i, j, 0});
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int y = current[0];
            int x = current[1];
            day = Math.max(day, current[2]);

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (ny < 0 || ny >= n || nx < 0 || nx >= m || tomato[ny][nx] != 0) {
                    continue;
                }

                queue.offer(new int[] {ny, nx, current[2] + 1});
                tomato[ny][nx] = 1;
                count--;
            }
        }

        if (count > 0) {
            return -1;
        }

        return day;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[][] tomato = new int[n][m];
        int count = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                tomato[i][j] = Integer.parseInt(st.nextToken());

                if (tomato[i][j] == 0) {
                    count++;
                }
            }
        }

        int result = bfs(m, n, count, tomato);
        System.out.println(result);
    }
}
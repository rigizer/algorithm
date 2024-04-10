import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dy = {0, 1};
    static int[] dx = {1, 0};

    static class Node {
        int y;
        int x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    private static boolean bfs(int n, int[][] board) {
        Queue<Node> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];

        queue.offer(new Node(0, 0));
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            int ny = node.y;
            int nx = node.x;

            if (board[ny][nx] == -1) {
                return true;
            }

            for (int d = 0; d < 2; d++) {
                int y = ny + dy[d] * board[ny][nx];
                int x = nx + dx[d] * board[ny][nx];

                if (y < 0 || y >= n || x < 0 || x >= n) {
                    continue;
                }
                
                if (visited[y][x] == false) {
                    queue.offer(new Node(y, x));
                    visited[y][x] = true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(bfs(n, board) ? "HaruHaru" : "Hing");
    }
}
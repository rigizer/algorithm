import java.util.*;

public class Main {
    static class Node {
        int z;
        int y;
        int x;

        Node(int z, int y, int x) {
            this.z = z;
            this.y = y;
            this.x = x;
        }
    }

    public static Queue<Node> queue = new LinkedList<>();
    public static char[][][] board;
    public static int[][][] visited;

    public static int[] dz = {1, 0, 0, 0, 0};
    public static int[] dy = {0, -1, 1, 0 ,0};
    public static int[] dx = {0, 0, 0, -1, 1};

    private static int bfs(int h, int m, int n) {
        while (!queue.isEmpty()) {
            Node node = queue.poll();

            int nz = node.z;
            int ny = node.y;
            int nx = node.x;

            for (int d = 0; d < 5; d++) {
                int z = nz + dz[d];
                int y = ny + dy[d];
                int x = nx + dx[d];

                if (z >= h || 0 > y || y >= m || 0 > x || x >= n) {
                    continue;
                }

                if (board[z][y][x] == '.' && visited[z][y][x] > visited[nz][ny][nx] + 5) {
                    queue.offer(new Node(z, y, x));
                    visited[z][y][x] = visited[nz][ny][nx] + 5;
                }
                else if (board[z][y][x] == '2') {
                    return visited[nz][ny][nx] + 5;
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();
        int n = sc.nextInt();

        board = new char[h][m][n];
        visited = new int[h][m][n];

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = sc.next().toCharArray();
                Arrays.fill(visited[i][j], Integer.MAX_VALUE);
                for (int k = 0; k < n; k++) {
                    if (board[i][j][k] == '1') {
                        queue.offer(new Node(i, j, k));
                        visited[i][j][k] = 0;
                    }
                }
            }
        }

        int result = bfs(h, m, n);
        System.out.println(result);
    }
}
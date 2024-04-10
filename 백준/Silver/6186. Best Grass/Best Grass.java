import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, 1, 0, -1};

    static class Node {
        int y;
        int x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    private static int bfs(int r, int c, char[][] board) {
        int result = 0;

        Queue<Node> queue = new LinkedList<>();
        boolean[][] visited = new boolean[r][c];

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == '.' || visited[i][j] == true) {
                    continue;
                }

                queue.offer(new Node(i, j));
                visited[i][j] = true;
                result++;

                while (!queue.isEmpty()) {
                    Node node = queue.poll();

                    int ny = node.y;
                    int nx = node.x;

                    for (int d = 0; d < 4; d++) {
                        int y = ny + dy[d];
                        int x = nx + dx[d];

                        if (y < 0 || r <= y || x < 0 || c <= x || visited[y][x] == true) {
                            continue;
                        }

                        if (board[y][x] == '#') {
                            queue.offer(new Node(y, x));
                            visited[y][x] = true;
                        }
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        char[][] board = new char[r][c];

        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }

        System.out.println(bfs(r, c, board));
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static class Node {
        private int y;
        private int x;
        
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    
    private static int bfs(int i, int j, int r, int c, char[][] board, boolean[][] visited) {
        int space = 0;
        
        Queue<Node> queue = new LinkedList<>();
        
        queue.offer(new Node(i, j));
        visited[i][j] = true;
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            space++;
            
            for (int d = 0; d < 4; d++) {
                int y = node.y + dy[d];
                int x = node.x + dx[d];
                
                if (y < 0 || y >= r || x < 0 || x >= c || board[y][x] != '.' || visited[y][x] == true) {
                    continue;
                }
                
                queue.offer(new Node(y, x));
                visited[y][x] = true;
            }
        }
        
        return space;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int tc = Integer.parseInt(br.readLine());
        
        for (int t = 1; t <= tc; t++) {
            st = new StringTokenizer(br.readLine());
            
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            char[][] board = board_init(r, c, br);
            boolean[][] visited = new boolean[r][c];
            
            int section = 0;
            int space = 0;
            
            // 상자의 섹션과 각 공간의 수 확인
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (board[i][j] == '.' && visited[i][j] == false) {
                        section++;
                        space += bfs(i, j, r, c, board, visited);
                    }
                }
            }
            
            StringBuilder sb = new StringBuilder();
            sb.append(section == 1 ? String.format("%d section, ", section) : String.format("%d sections, ", section));
            sb.append(space == 1 ? String.format("%d space", space) : String.format("%d spaces", space));
            
            System.out.println(sb.toString());
        }
    }
    
    private static char[][] board_init(int r, int c, BufferedReader br) throws IOException {
        char[][] board = new char[r][c];
        
        for (int i = 0; i < r; i++) {
            board[i] = br.readLine().toCharArray();
        }
        
        return board;
    }
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
    static int[] dy = {-1, 0, 1, 0};
    static int[] dx = {0, 1, 0, -1};
    
    static class Node {
        int y;
        int x;
        int t;
        
        Node(int y, int x, int t) {
            this.y = y;
            this.x = x;
            this.t = t; // t == 0이면 #, t == 1이면 .
        }
    }
    
    private static boolean check(int n, int m, char[][] a, Queue<Node> queue, boolean[][] visited) {
        while(!queue.isEmpty()) {
            Node node = queue.poll();
            
            int ny = node.y;
            int nx = node.x;
            int nt = node.t;
            
            for (int d = 0; d < 4; d++) {
                int y = ny + dy[d];
                int x = nx + dx[d];
                
                if (0 <= y && y < n && 0 <= x && x < m && visited[y][x] == false) {
                    if (nt == 0 && a[y][x] == '#') {
                        return false;
                    } else if (nt == 1 && a[y][x] == '.') {
                        return false;
                    }
                    
                    queue.offer(new Node(y, x, nt == 0 ? 1 : 0));
                    visited[y][x] = true;
                }
            }
        }
        
        return true;
    }
    
    private static boolean calc(int n, int m, char[][] a) {
        Queue<Node> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] == '#' && visited[i][j] == false) {
                    queue.offer(new Node(i, j, 0));
                    visited[i][j] = true;
                } else if (a[i][j] == '.' && visited[i][j] == false) {
                    queue.offer(new Node(i, j, 1));
                    visited[i][j] = true;
                }
                
                if (check(n, m, a, queue, visited) == false) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int t = Integer.parseInt(br.readLine());
        
        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            
            char[][] a = new char[n][m];
            for (int i = 0; i < n; i++) {
                a[i] = br.readLine().toCharArray();
            }
            
            boolean result = calc(n, m, a);
            System.out.println(String.format("#%d %s", tc, result ? "possible" : "impossible"));
        }
    }
}
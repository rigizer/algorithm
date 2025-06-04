import java.io.*;

public class Main {
    static char[][] map;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        map = new char[n][2 * n - 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2 * n - 1; j++) {
                map[i][j] = ' ';
            }
        }

        drawStar(n, 0, n - 1);
        
        for (char[] row: map) {
            sb.append(row).append("\n");
        }
        System.out.print(sb);
    }

    public static void drawStar(int n, int x, int y) {
        if (n == 3) {
            map[x][y] = '*';
            map[x + 1][y - 1] = '*';
            map[x + 1][y + 1] = '*';
            for (int i = -2; i <= 2; i++) {
                map[x + 2][y + i] = '*';
            }
            return;
        }

        int half = n / 2;
        drawStar(half, x, y);
        drawStar(half, x + half, y - half);
        drawStar(half, x + half, y + half);
    }
}
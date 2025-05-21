import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        char[][] cloud = new char[h][w];
        int[][] result = new int[h][w];

        for (int i = 0; i < h; i++) {
            cloud[i] = br.readLine().toCharArray();
            Arrays.fill(result[i], -1);
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (cloud[i][j] == 'c') {
                    result[i][j] = 0;
                } else if (j > 0 && result[i][j - 1] >= 0) {
                    result[i][j] = result[i][j - 1] + 1;
                }
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                sb.append(result[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] hw = br.readLine().split(" ");
        int h = Integer.parseInt(hw[0]);
        int w = Integer.parseInt(hw[1]);

        char[][] cloud = new char[h][w];
        int[][] result = new int[h][w];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < h; i++) {
            cloud[i] = br.readLine().toCharArray();
            Arrays.fill(result[i], -1);
        }

        for (int i = 0; i < h; i++) {
            int time = -1;
            for (int j = 0; j < w; j++) {
                if (cloud[i][j] == 'c') {
                    time = 0;
                } else if (time != -1) {
                    time++;
                }
                result[i][j] = time;
            }
        }

        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                sb.append(result[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}

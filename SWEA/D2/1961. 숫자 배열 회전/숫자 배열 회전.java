import java.io.*;
import java.util.*;

public class Solution {
    private static void rotate(int[][][] ns, int x, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ns[x][i][j] = ns[x - 1][n - j - 1][i];
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            int n = Integer.parseInt(br.readLine());
            int[][][] ns = new int[4][n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    ns[0][i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int x = 1; x <= 3; x++) {
                rotate(ns, x, n);
            }

            System.out.println("#" + tc);
            for (int i = 0; i < n; i++) {
                for (int j = 1; j <= 3; j++) {
                    for (int k = 0; k < n; k++) {
                        System.out.print(ns[j][i][k]);
                    }
                    System.out.print(" ");
                }
                System.out.println();
            }
        }
    }
}
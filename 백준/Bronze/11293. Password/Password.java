import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        for (int c = 1; c <= n; c++) {
            sb.append("Customer ").append(c).append("\n");
            int a = Integer.parseInt(br.readLine());
            char[][] ans = new char[a][];
            for (int i = 0; i < a; i++) {
                ans[i] = br.readLine().replace(" ", "").toCharArray();
            }

            int l = Integer.parseInt(br.readLine());
            for (int i = 0; i < l; i++) {
                st = new StringTokenizer(br.readLine());

                int target = Integer.parseInt(st.nextToken()) - 1;
                int x = Integer.parseInt(st.nextToken()) - 1;
                int y = Integer.parseInt(st.nextToken()) - 1;

                char xx = st.nextToken().charAt(0);
                char yy = st.nextToken().charAt(0);

                if (xx == ans[target][x] && yy == ans[target][y]) {
                    sb.append("correct").append("\n");
                } else {
                    sb.append("error").append("\n");
                }
            }
        }

        System.out.print(sb);
    }
}
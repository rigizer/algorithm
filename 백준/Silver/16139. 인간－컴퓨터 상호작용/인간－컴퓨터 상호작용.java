import java.io.*;
import java.util.*;

public class Main {
    private static int[][] calc(char[] s) {
        int[][] count = new int[26][s.length];
        for (int i = 0; i < 26; i++) {
            count[i][0] = (s[0] - 'a' == i) ? 1 : 0;
            for (int j = 1; j < s.length; j++) {
                count[i][j] = count[i][j - 1] + ((s[j] - 'a' == i) ? 1 : 0);
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        char[] s = br.readLine().toCharArray();
        int[][] k = calc(s);

        int q = Integer.parseInt(br.readLine());
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            char a = st.nextToken().charAt(0);
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            int idx = a - 'a';
            int result = k[idx][r] - (l > 0 ? k[idx][l - 1] : 0);
            sb.append(result).append('\n');
        }

        System.out.println(sb);
    }
}

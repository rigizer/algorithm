import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int lastNBit = (1 << (n)) - 1;
            if (lastNBit == (m & lastNBit)) {
                System.out.println("#" + tc + " ON");
            } else {
                System.out.println("#" + tc + " OFF");
            }
        }
    }
}
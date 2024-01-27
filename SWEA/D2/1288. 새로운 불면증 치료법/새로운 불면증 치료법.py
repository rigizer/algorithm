import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            int n = Integer.parseInt(br.readLine());
            boolean[] nums = new boolean[10];

            int m = 1;
            while (true) {
                int q = n * m;
                while (q > 0) {
                    int r = q % 10;
                    q /= 10;

                    nums[r] = true;
                }

                boolean check = true;
                for (int i = 0; i < 10; i++) {
                    if (nums[i] == false) {
                        check = false;
                        break;
                    }
                }

                if (check == true) {
                    System.out.println("#" + tc + " " + (n * m));
                    break;
                }

                m += 1;
            }
        }
    }
}
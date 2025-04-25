import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int[] ns = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            ns[i] = Integer.parseInt(st.nextToken());
        }

        int i = a;
        int result = 0;
        for (int num = 0; num < n; num++) {
            if (ns[num] == i) {
                result++;
                i += d;
            }
        }

        System.out.println(result);
    }
}
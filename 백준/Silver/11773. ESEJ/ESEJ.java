import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Math.max(a , (int) Math.ceil(Double.valueOf(b).doubleValue() / 2));

        for (int i = 0; i < c; i++) {
            int number = i;
            StringBuilder sb = new StringBuilder();
            while (number >= 0) {
                sb.insert(0, (char) ('a' + number % 26));
                number = number / 26 - 1;
            }

            System.out.print(sb.toString() + " ");
        }
    }
}

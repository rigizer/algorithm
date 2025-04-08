import java.io.*;
import java.util.*;

class Main {
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader I = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter O = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder a = new StringBuilder();
        StringTokenizer s = new StringTokenizer(I.readLine());

        int q = Integer.parseInt(s.nextToken()), w = Integer.parseInt(s.nextToken());
        int m = 100000000, ax = 0, ay = 0;
        int e = w / q;

        for (int i = 1; i * i <= e; i++) {
            if (e % i == 0) {
                int x = i;
                int y = e / i;

                if (gcd(x, y) == 1) {
                    int a1 = x * q;
                    int a2 = y * q;

                    if (a1 + a2 < m) {
                        m = a1 + a2;
                        ax = Math.min(a1, a2);
                        ay = Math.max(a1, a2);
                    }
                }
            }
        }

        a.append(ax).append(' ').append(ay);
        O.write(a + "\n");
        O.flush();
    }
}
